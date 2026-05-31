def apply_discount(price, discount):

    if type(price) != float and type(price) != int:
        return("The price should be a number")
    elif type(discount) != float and type(discount) != int:
        return("The discount must be a number")
    elif price <= 0 :
        return("The price should be greater than 0")
    elif discount < 0 or discount > 100 :
        return("The discount should be between 0 and 100")
    else:
        return(price - discount/100*price)
