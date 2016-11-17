<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>
   <xsl:template match="/">
       <html>
            <body>
                <h1><xsl:value-of select="/product/description/name"/></h1>
                <table border="1">
                        <th>
       <xsl:apply-templates select="product"/>
                        </th>
                     </table>
            </body>
       </html>
   </xsl:template>
     <xsl:template match="product">
        <tr>
                   <td width="80">product ID</td>
                   <td><xsl:value-of select="@pid"/></td>
              </tr>
              <tr>
                   <td width="200">product name</td>
                   <td><xsl:value-of select="/product/description/name"/></td>
              </tr>
              <tr>
                   <td width="200">price</td>
                   <td>$<xsl:value-of select="/product/description/price"/></td>
              </tr>
              <tr>
                   <td width="50">details</td>
                   <td><xsl:value-of select="/product/description/details"/></td>
              </tr>
  </xsl:template>
</xsl:stylesheet>
