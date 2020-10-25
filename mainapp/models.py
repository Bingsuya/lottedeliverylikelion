from django.db import models

# Create your models here.

class Box(models.Model):
    box_type = models.BooleanField() # True = 받는 False = 보내는
    code = models.CharField(max_length = 30) # 송장번호
    company = models.CharField(max_length = 30) # 택배사
 
    sender = models.CharField(max_length = 30) # 보내는사람 이름
    sender_phone = models.CharField(max_length = 30) # 보내는사람 전화번호
    sender_address = models.CharField(max_length = 100) # 보내는사람 주소
    
    receiver =  models.CharField(max_length = 30) # 받는사람 이름
    receiver_phone = models.CharField(max_length = 30) # 받는사람 전화번호
    receiver_address = models.CharField(max_length = 100) # 받는사람 주소

    box_detail = models.CharField(max_length = 30) # 상품정보
    worker = models.CharField(max_length = 30, default ="미정") # 배송기사 이름
    worker_phone = models.CharField(max_length = 30, default = " ") # 배송기사 전화번호
    visit_date = models.DateTimeField(null = True)# 택배 예약시 방문희망일
    box_step = models.CharField(max_length = 30)

    create_date = models.DateTimeField(null = True, auto_now_add=True)    #예약생성일자변수추가
    box_value = models.CharField(max_length = 30 ,null = True) #물품 가액
    box_size = models.CharField(max_length = 30 ,null = True) #물품 크기
    box_amount = models.CharField(max_length = 30 ,null = True) #물품 개수
    box_pay = models.CharField(max_length = 30 ,null = True) #결제 방법 , 착(post)/선불(pre)
    
class Location(models.Model):
    name = models.CharField(max_length = 30) # 위치
    lo = models.CharField(max_length = 50) # 경도
    la = models.CharField(max_length = 50) # 위도
    des = models.TextField() # 마커 설명 

    def __str__(self):
        return self.name
class State(models.Model):
    step = models.CharField(max_length = 50)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    box_date = models.DateTimeField()
    box_now = models.ForeignKey(Location, on_delete=models.CASCADE)
    box_state = models.CharField(max_length = 30)
    box_latest = models.BooleanField(default=True)
    # @property
    # def latest_state(self,box):
    #     states=State.objects.filter(box=box).order_by('box_date')
    #     return states[0]
            


