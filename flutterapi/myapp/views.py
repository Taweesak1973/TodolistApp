from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#GET data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()#ดึงข้อมูลจาก todolist
    serializer =TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

#POST Data(save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method=='POST':
        serializer=TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

#PUT Data(Updata Data)
@api_view(['PUT'])
def update_todolist(request,TID):
    todo=Todolist.objects.get(id=TID)
    
    if request.method == 'PUT':
        data={}
        serializer=TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


#DELETE (Delete Data)
@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo=Todolist.objects.get(id=TID)
    
    if request.method=='DELETE':
        delete=todo.delete()
        data={}
        if delete:
            data['status']='deleted'
            statuscode=status.HTTP_200_OK
        else:
            data['status']='fail'
            statuscode=status.HTTP_400_BAD_REQUEST
        
        return Response(data=data, status=statuscode)



data=[
{
    "title":"คอมพิวเตอร์คืออะไร?",
    "subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
    "image_url":"https://cdn.pixabay.com/photo/2016/11/29/06/18/home-office-1867761_960_720.jpg",
    "detail":"   วิทยาการคอมพิวเตอร์ หรือ วิทยาศาสตร์คอมพิวเตอร์ (อังกฤษ: computer science หรือ informatics) เป็นศาสตร์เกี่ยวกับการศึกษาค้นคว้า....ทฤษฎีการคำนวณสำหรับคอมพิวเตอร์ และทฤษฎีการประมวลผลสารสนเทศข้อมูล ทั้งด้านซอฟต์แวร์ ฮาร์ดแวร์ และ เครือข่าย วิทยาการคอมพิวเตอร์มีความเกี่ยวโยงกับทฤษฎีการคำนวณ อัลกอริทึม ปัญหาด้านการคำนวณ การออกแบบฮาร์ดแวร์ ซอฟต์แวร์ และ แอปพลิเคชัน\n\n วิทยาการคอมพิวเตอร์ศึกษาเกี่ยวกับกระบวนการประมวลผลข้อมูล ทั้งในสิ่งมีชีวิตตามกระบวนการธรรมชาติ และ ระบบคอมพิวเตอร์ที่มนุษย์สร้างขึ้น เช่น การสื่อสาร การควบคุม การรับรู้ การเรียนรู้ และ สติปัญญา โดยเฉพาะในคอมพิวเตอร์สาขาวิชาวิทยาการคอมพิวเตอร์ สามารถแบ่งออกเป็น 2 ภาค ได้แก่ ภาคทฤษฎี ซึ่งมีความเป็นนามธรรมสูง เช่น การวิเคราะห์และสังเคราะห์ขั้นตอนวิธี ทฤษฎีความซับซ้อนของการคำนวณ ไปจนถึงภาคปฏิบัติ ที่เน้นการใช้งานที่เป็นรูปธรรม เช่น ทฤษฎีภาษาโปรแกรม ทฤษฎีการพัฒนาซอฟต์แวร์ ทฤษฎีฮาร์ดแวร์คอมพิวเตอร์ คอมพิวเตอร์กราฟิก และ ทฤษฎีเครือข่ายอัลกอริทึม คือ หัวใจของวิทยาศาสตร์คอมพิวเตอร์ ทฤษฎีภาษาโปรแกรม พิจารณาแนวทางในการอธิบายกระบวนการคำนวณ\n\n ในขณะที่วิศวกรรมซอฟต์แวร์เกี่ยวข้องกับการใช้ภาษาโปรแกรมและระบบที่ซับซ้อน สถาปัตยกรรมคอมพิวเตอร์และวิศวกรรมคอมพิวเตอร์เกี่ยวข้องกับการสร้างส่วนประกอบคอมพิวเตอร์และอุปกรณ์ที่ควบคุมด้วยคอมพิวเตอร์ การศึกษาปฏิสัมพันธ์ระหว่างมนุษย์กับคอมพิวเตอร์ พิจารณาถึงความท้าทายในการทำให้คอมพิวเตอร์มีประโยชน์ใช้งานได้และสามารถเข้าถึงได้ ปัญญาประดิษฐ์มีจุดมุ่งหมายเพื่อสังเคราะห์กระบวนการเพื่อการแก้ปัญหา การตัดสินใจ การปรับตัวกับสิ่งแวดล้อม การวางแผน การเคลื่อนไหว การเรียนรู้ และ การสื่อสาร แบบสิ่งมีชีวิตทรงภูมิปัญญาวิทยาการคอมพิวเตอร์ ในฐานะศาสตร์การศึกษานั้น นับเป็นหนึ่งใน 5 สาขาวิชาคอมพิวเตอร์ ประกอบด้วย วิทยาการคอมพิวเตอร์ วิศวกรรมคอมพิวเตอร์ วิศวกรรมซอฟต์แวร์ เทคโนโลยีสารสนเทศ และ ระบบสารสนเทศ"
},
{
    "title":"มาเขียนโปรแกรมกัน!",
    "subtitle":"บทความนี้จะแนะนำการเริ่มต้นเขียนโปรแกรม",
    "image_url":"https://cdn.pixabay.com/photo/2014/03/22/22/17/phone-292994_960_720.jpg",
    "detail":"   การเขียนโปรแกรมคอมพิวเตอร์ (อังกฤษ: Computer programming) หรือเรียกให้สั้นลงว่า การเขียนโปรแกรม (อังกฤษ: Programming) หรือ การเขียนโค้ด (Coding) เป็นขั้นตอนการเขียน ทดสอบ และดูแลซอร์สโค้ดของโปรแกรมคอมพิวเตอร์ ซึ่งซอร์สโค้ดนั้นจะเขียนด้วยภาษาโปรแกรม ขั้นตอนการเขียนโปรแกรมต้องการความรู้ในหลายด้านด้วยกัน เกี่ยวกับโปรแกรมที่ต้องการจะเขียน และขั้นตอนวิธีที่จะใช้ ซึ่งในวิศวกรรมซอฟต์แวร์นั้น การเขียนโปรแกรมถือเป็นเพียงขั้นหนึ่งในวงจรชีวิตของการพัฒนาซอฟต์แวร์\n\n\tการเขียนโปรแกรมจะได้มาซึ่งซอร์สโค้ดของโปรแกรมนั้นๆ โดยปกติแล้วจะอยู่ในรูปแบบของ ข้อความธรรมดา ซึ่งไม่สามารถนำไปใช้งานได้ จะต้องผ่านการคอมไพล์ตัวซอร์สโค้ดนั้นให้เป็นภาษาเครื่อง (Machine Language) เสียก่อนจึงจะได้เป็นโปรแกรมที่พร้อมใช้งาน\n\n\tการเขียนโปรแกรมถือว่าเป็นการผสมผสานกันระหว่างศาสตร์ของ ศิลปะ วิทยาศาสตร์ คณิตศาสตร์ และ วิศวกรรม เข้าด้วยกัน [1]"

},

{
    "title":"Flutter คืออะไร?",
    "subtitle":"Tools สำหรับออกแบบ UI ของ Google",
    "image_url":"https://media.istockphoto.com/photos/word-dart-on-paper-and-laptop-picture-id1316473219?s=612x612",
    "detail":"   Flutter คือ Framework ที่ใช้สร้าง UI สำหรับ mobile application ที่สามารถทำงานข้ามแพลตฟอร์มได้ทั้ง iOS และ Android ในเวลาเดียวกัน โดยภาษาที่ใช้ใน Flutter นั้นจะเป็นภาษา dart ซึ่งถูกพัฒนาโดย Google และที่สำคัญคือเป็น open source ที่สามารถใช้งานได้แบบฟรี ๆ อีกด้วย"
}
]

# json_dumps_params={'ensure_ascii':False}#ไม่ใช้ก็ได้ถ้าข้อความไม่มีปัญหาในกาแสดงผลหน้าเวบ
def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
