
class helper:

    #this page has helper methods
    # Helper methods
    def safe_float(self, value):
        try:
            # Remove commas and convert to float
            return float(value.replace(',', ''))
        except ValueError:
            # Handle invalid float values
            return None


    def safe_int(self, value):
        try:
            # Remove commas and convert to integer
            return int(value.replace(',', ''))
        except ValueError:
            # Handle invalid integer values
            return None