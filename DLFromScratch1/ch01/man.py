class Man:                    # Man이라는 새로운 클래스를 정의
    def __init__(self,name):  # 생성자(초기화 메서드)는 name이라는 인수를 받음
        self.name = name      # 받은 인수로 인스턴스 변수인 self.name을 초기화함
        print("Initialized!") #  * 인스턴스 변수 - 인스턴스별로 저장되는 변수
    def hello(self):          #               - self 다음에 속성 이름을 써서 작성하거나 접근 가능
        print("Hello " + self.name + "!")
    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")              # m이라는 인스턴스(객체) 생성
m.hello()
m.goodbye()