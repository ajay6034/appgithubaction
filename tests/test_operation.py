from src.mathoperations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(5,-3)==2
    assert add(5,6)==11

def test_sub():
    assert sub(5,3)==2
    assert sub(3,3)==0
    assert sub(8,5)==3
    
