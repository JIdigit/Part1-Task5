def bigger_guys(one,two):
    while one>two:
        return one
    else: 
        return two
def test_bigger_guy():
    assert bigger_guys(1, 2) == 2
    assert bigger_guys(10, 20) == 20
    assert bigger_guys(20, 10) == 20
    assert bigger_guys(10, 10) == 10
    assert bigger_guys(2, 1) == 2
    assert bigger_guys('a', 'b') == 'b' # 'b' is greater than 'a'
    print("YOUR CODE IS CORRECT!")
test_bigger_guy()