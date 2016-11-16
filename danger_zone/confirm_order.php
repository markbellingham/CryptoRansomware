<?php
require_once ("../includes/session.php");
require_once ("../includes/db_connection.php");
require_once ("../includes/functions.php");

$page_title = 'Confirm Order | HyperAV';
include ("../includes/layouts/header.php");

// If the user somehow got here without being logged in, they are redirected to the login page
if(!isset($_SESSION['cuEmail']) && !isset($_SESSION['staff'])) {
	redirect_to("login_page.php");
}

// Gets the cart from the SESSION
if (isset($_SESSION['cart'])) {
	$cart = $_SESSION['cart'];
} else {
	// If the user somehow got here without making an order, they are redirected to the products page
	redirect_to("products.php");
}

// Create SQL statement from the $cart array
if (count($cart) > 0) {
	// First get the productIDs from the array
	$cart_keys = array_keys($cart);
	$query = 'SELECT * FROM hyperav_products WHERE ';
	// Build up a SELECT  statement from all the items in the array
	for ($i = 0; $i < count($cart); $i++) {
		if ($i != 0) {
			$query .= ' OR ';
		}
		$query .= 'prModelNo = "' . $cart_keys[$i] . '"';
	}
} else {

}


// Send the query to the database
$results = @mysqli_query($connection, $query);
$num_rows = mysqli_num_rows($results);

// Display the results (if any) in a form to submit the order to the database
echo '<form action="confirm_order_submit.php" method="POST">';
if ($results) {
	if ($num_rows > 0) {
		$grandTotal = 0;
		echo '<p><h3>Confirm your order</h3></p>';
		echo '<div style="float: left; margin-left: 10px;">';
		echo '<table class="results"><tr><th></th><th><b>Name</b></th><th><b>Price per item</b></th><th><b>Quantity</b></th><th><b>Total per item</b></th><th></th></tr>';
		while ($row = mysqli_fetch_array($results, MYSQLI_ASSOC)) {
			$ID = $row['prModelNo'];
			echo '<tr><td><img src="images/' . $row['prName'] . '.jpg" id="product_images"></td>
				<td><a href="selected_product.php?prModelNo=' . $row['prModelNo'] . '">' . $row['prName'] . '</a></td>
				<td>&pound' . $row['prPrice'] . '</td>
				<td>' . $cart[$ID] . '</td>';
			// Calculate the total cost of each item when multiplied by the quantity
			$totalPerItem = (($row['prPrice']) * (int)$cart[$ID]);
			echo '<td>&pound' . number_format($totalPerItem,2) . '</td></tr>';
			$grandTotal += $totalPerItem;
		}
		echo '<tfoot><td colspan="4"><b>Total</td><td><b>&pound' . number_format($grandTotal,2) . '</b></td></tfoot>';
		$_SESSION['grandTotal'] = $grandTotal;
		echo '</table>';
		echo '</div>';

		mysqli_free_result($results);
	}
}

/* Shows the customer information or asks the staff member for the email address,
 then when the staff member clicks on the confirm button, the customer's address is shown for checking. */
echo '<div style="float: left; margin-left: 50px;">';
if (isset($_SESSION['cuEmail'])) {
	// Get the customer information from the database
	$query1 = 'SELECT * FROM hyperav_customer WHERE cuEmail = "' . $_SESSION['cuEmail'] . '"';
	$results1 = @mysqli_query($connection, $query1);
	$num_rows1 = mysqli_num_rows($results1);

	// Get the results (if any)
	if ($results1) {
		if ($num_rows1 > 0) {

			echo '<p><b>Are your details correct?</b></p>';
			while ($row = mysqli_fetch_array($results1, MYSQLI_ASSOC)) {
				$customerID = $row['customerID'];
				echo '<p>' . $row['cuFName'] . ' ' . $row['cuLName'] . '</p>';
				echo '<p>' . $row['cuAddress1'] . '</p>';
				echo '<p>' . $row['cuAddress2'] . '</p>';
				echo '<p>' . $row['cuTown'] . '</p>';
				echo '<p>' . $row['cuPostcode'] . '</p>';
			}
		} else {
			echo 'We couldn\'t find your details, please check your email address';
			echo '<p>Please confirm the customer\'s email address:</p>';
			echo '<input type="email" name="cuEmail" required>';
		}

		mysqli_free_result($results1);
	} else {
		// If there wasa a problem with the database query itself, we end up here.
		echo '<h3 class="error">System Error</h3>
		<p class="error">Product data could not be retrieved.</p>';
		//DEBUGGING echo '<p class="error">'.mysqli_error($connection).'</p>';
		//DEBUGGING echo '<p class="error">Query:'. $query . '</p>';
	}
} else if (isset($_SESSION['staff']) && !isset($_SESSION['cuEmail'])) {
	echo '<p>Please confirm the customer\'s email address:</p>';
	echo '<input type="email" name="cuEmail" required>';
}

/* If the customer is making the order, provide a dropdown box
 so that they can choose a location for pickup or delivery
 If a staff member is placing the order on behalf of the customer,
 The location is taken from the location the staff member works at. */
echo '<br />';
if (isset($_SESSION['cuEmail']) && !isset($_SESSION['staff'])) {
	echo '<p><b>Please choose a location for pickup or delivery</b></p>';
	$query2 = "SELECT DISTINCT loName FROM hyperav_location ORDER BY loName ASC";
	$results2 = @mysqli_query($connection, $query2);
	$num_rows2 = mysqli_num_rows($results2);
	if($results2) {
		if($num_rows2 > 0) {?>
			<select name="location">
				<option>Select Location</option>
				<?php while($option = mysqli_fetch_array($results2, MYSQLI_ASSOC)) { ?>
					<option><?php echo $option['loName']; ?></option>
			<?php } ?>
			</select><?php
		}

		mysqli_free_result($results2);
	}
}

mysqli_close($connection);
?>
<p><b>Please select payment type</b></p>
<select name="payment">
	<option>Credit Card</option>
	<option>Debit Card</option>
	<option>Cash</option>
</select>

</div>

<div style="clear: both"><p><input type="submit" value="Confirm Order"></p></div>
</form>