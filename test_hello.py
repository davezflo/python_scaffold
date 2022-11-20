import hello
def test_add():
    assert hello.add(10,10)==20
    
def test_add_negative():
    assert hello.add(10,20)!=40