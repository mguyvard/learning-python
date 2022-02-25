def make_car(manufacturer, model_name, **options):
    '''Defines a dictionary about a car'''
    car_dic = {
        'manufacturer': manufacturer.title(),
        'model': model_name.title(),
        }    
    
    for option, value in options.items():
        car_dic[option] = value
        
    return car_dic


        

