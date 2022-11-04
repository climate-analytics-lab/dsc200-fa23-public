class Food:
    '''
        Cost in USD for each item
    '''
    food_dict = {
        'Fries':9.99,
        'Burger':12.99,
        'Tacos':10.99,
        'Wings':12.99,
        'Slider':10.99
    }
    '''
        Preparation time in minutes
    '''
    food_prep_time = {
        
        'Fries':5,
        'Burger':7,
        'Tacos':7,
        'Wings':8,
        'Slider':6
    }
    def __init__(self,food_item,quantity):
        '''
        Initialize a Food object 
        Note: Quantity will always be an integer.
        
        A Food object should have the following attributes:
        food_item
        quantity
        cost
        prep_time
        '''
        self.food_item = None
        self.quantity = None
        self.cost = None
        self.prep_time = None
        ...

class Drink:
    drinks = ['Coke','Diet Coke','Pepsi']
    size_dict = {
        'small':3.99,
        'medium':4.99,
        'large':5.99
    }
    '''
        Preparation time in minutes
    '''
    drink_prep_time = {
        
        'Coke':1,
        'Diet Coke':1,
        'Pepsi':1
    }
    def __init__(self,drink_item, size):
        '''
        Initialize a Drink object 
        
        A Drink object should have the following attributes:
        drink_item
        size
        cost
        prep_time
        '''
        self.drink_item = None
        self.size = None
        self.cost = None
        self.prep_time = None
        ...

class Order:
    '''
    This is a generic parent class
    An Order can consist of several items from the Food and Drinks class.
    An Order object has the following attributes
    1. items : List that contains Food and Drink objects
    2. order_id : Integer that is passed to the constructor of the Order class. Refer to the example below for more clarification.
    3. timestamp : A time reference for when the order is placed. This is also passed to the class constructor as an argument.
    4. prep_time : The total time required to prepare the order. Add up the prep time from all the Drinks and Food Object. Prep time should be updated after every item is added or removed.
    '''
    def __init__(self,order_id, timestamp):
        self.items = None
        self.order_id = None
        self.timestamp = None
        self.prep_time = None
        ...
    def computeTotalPrepTime(self):
        '''
        Calculate total prep time for the order
        '''
        ...
        
    def computeCost(self):
        '''
        Calculate total cost for the order
        '''
        ...
    def addItem(self, item_type, item_name, item_size):
        '''
        arguments:
        item_type: Type of item ordered, can be either Food or Drink
        item_name: Name of the item ordered. If the item is not available, return 'Item Unavailable'.
        item_size: Size/Quantity of the item ordered. For Food this argument acts as the number of items ordered. For Drinks this argument acts as the size of the drink
                   If the drink size is not available return 'Size Unavailable'
        '''
        ...
