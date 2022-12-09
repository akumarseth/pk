
def test_exc():
    try:
        result = int('safsdgfsdgfs')
        print(result)
        
    except ZeroDivisionError as z:
        print("line no 6 exception occured", str(z))
    except Exception as e:
        print('line no 8', str(e))
    finally:
        print('finally block')


test_exc()