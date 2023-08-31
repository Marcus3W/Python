from datetime import datetime

# Import random below:
import random



# DATETIME
current_time = datetime.now()
print(current_time)

# RANDOM
# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)]
# Create randomer_number below:
randomer_number = random.choice(random_list)
# Print randomer_number below:
print(randomer_number)


# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

