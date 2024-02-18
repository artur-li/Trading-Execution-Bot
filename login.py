import MetaTrader5 as mt5

class Login:
    def __init__(self, username=5022907425, password="@hQhZ8Sq", server="MetaQuotes-Demo"):
        """
        Initialize the Login object with default or provided credentials.
        """
        self.username = username
        self.password = password
        self.server = server
    
    def login(self):
        """
        Perform the login process to MetaTrader 5.
        """
        print("Initializing login to MetaTrader 5...")
        
        # Initialize connection to MetaTrader 5
        if not mt5.initialize():
            print("Initialization failed. Error code:", mt5.last_error())
            return
        
        # Login to account
        authorized = mt5.login(self.username, password=self.password, server=self.server)
        if authorized:
            print(f"Successfully logged into account #{self.username}!")
        else:
            print(f"Failed to log in to account #{self.username}. Error code:", mt5.last_error())

login_obj = Login()
login_obj.login()
