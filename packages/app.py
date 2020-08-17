# import packages
# option 1 import the full package 
import ecommerce.shipping
# import something speciffec from package 
from ecommerce.shipping import calc_shipping
# option 3 import all function from package
from ecommerce import price


# in option 1 you have to type the package name 
ecommerce.shipping.calc_shipping()

# option 2 type only the function name
calc_shipping()


price.product_price()