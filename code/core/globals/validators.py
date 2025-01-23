from rest_framework.validators import ValidationError

def check_email_or_phonenumber (val:str) -> dict:
    # check if the val is email or phonenumber and return dict

    if val.startswith("+"):
        if not val[1::].isnumeric() : 
            ValidationError({
                'message' : 'invalid phonenumber'
            })
        return {
            'phonenumber' : val
        }
    
    elif '@' in val:
        return {
            'email' : val
        }
    else:
        ValidationError({
            'message' : 'invalid email or phonenumber'
        })