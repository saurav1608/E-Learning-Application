#!C:\Python34\python.exe
print("Content-Type: text/html\r\n\r\n")
import cgi, cgitb, sqlite3
import random
conn=sqlite3.connect('project.db')
a=random.sample(range(1,25), 10)
list=a
w=10
Matrix=[0 for m in range(w)]
Matrix1=[0 for m in range(w)]
Matrix2=[0 for m in range(w)]
Matrix3=[0 for m in range(w)]
Matrix4=[0 for m in range(w)]
Matrix5=[0 for m in range(w)]
cnt=0
for x in a:
    cursor=conn.execute('''SELECT * FROM QUETIONS where Sr=?;''',(x,))
    cursor=cursor.fetchone()  
    Matrix[cnt]=cursor[1]
    Matrix1[cnt]=cursor[2]
    Matrix2[cnt]=cursor[3]
    Matrix3[cnt]=cursor[4]
    Matrix4[cnt]=cursor[5]
    Matrix5[cnt]=cursor[6]
    cnt=cnt+1

conn.close()


print('<!DOCTYPE html>')
print('<html>')
print('<body>')
print('<style>')
print('div.container {')
print('width: 100%;')
print('height: 300px;')
print('font-size:20px;')
print('border: 1px solid gray;}')
print('div.container1 {')
print('width: 100%;')
print('height: 100px;')
print('border: 1px solid gray;')
print('}')
print('input[type=radio]{')
print('border: 0px;')
print('width: 5%;')
print('height: 2em;')
print('}')
print('.submit')
print('{')
print('height:200px;')
print('width:200px;')
print('}')
print('header {')
print('padding: 1em;')
print('color: white;')
print('background-color:gray;')
print('clear: left;')
print('text-align: center;')
print('}')
print('</style>')
print('</head>')
print('<body>')
print('<form id="test">')
print('<div class="container1">')
print('<header>')
print('<h1>WELCOME</h1>')
print('</header>')
print('</div class="container">')
print('<div class="container">')
print('<h3>1. </h3>')
print('<p id="p1">',Matrix[0],'</p>')
print('<input type="radio" name="r1" id="op1" value="a">',Matrix1[0])
print('<p id="Q1_1" style="display:none">',Matrix5,
'</p></input></br>')
print('<input type="radio" name="r1" id="op2" value="b">',Matrix2[0])
print('<p id="Q1_2" style="display:inline">')
print('</p></input></br>')   
print('<input type="radio" name="r1" id="op3" value="c">',Matrix3[0])
print('<p id="Q1_3" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r1" id="op4" value="d">',Matrix4[0])
print('<p id="Q1_4" style="display:inline"></p></input></br>')
print('</div>')
print('<div class="container">')
print('<h3>2. </h3>')
print('<p id="p2">',Matrix[1],'</p>')
print('<input type="radio" name="r2" id="op5" value="a">',Matrix1[1])
print('<p id="Q2_1" style="display:inline" ></p></input></br>')  
print('<input type="radio" name="r2" id="op6" value="b">',Matrix2[1])
print('<p id="Q2_2" style="display:inline"></p></input></br>')    
print('<input type="radio" name="r2" id="op7" value="c">',Matrix3[1])
print('<p id="Q2_3" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r2" id="op8" value="d">',Matrix4[1])
print('<p id="Q2_4" style="display:inline"></p></input></br>')   
print('</div>')
print('<div class="container">')
print('<h3>3. </h3>')
print('<p id="p3">',Matrix[2],'</p></br>')
print('<input type="radio" name="r3" id="op9" value="a">',Matrix1[2])
print('<p id="Q3_1" style="display:inline"></p></input></br>')
print('<input type="radio" name="r3" id="op10" value="b">',Matrix2[2])
print('<p id="Q3_2" style="display:inline" Value=Matrix3[2]></p></input></br>')   
print('<input type="radio" name="r3" id="op11" value="c">',Matrix3[2])
print('<p id="Q3_3" style="display:inline"></p></input></br>')    
print('<input type="radio" name="r3" id="op12" value="d">',Matrix4[2])
print('<p id="Q4_4" style="display:inline"></p></input></br>')   
print('</div>')
print('<div class="container">')
print('<h3>4. </h3>')
print('<p id="p4">',Matrix[3],'</p></br>')
print('<input type="radio" name="r4" id="op13" value="a">',Matrix1[3])
print('<p id="Q4_1" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r4" id="op14" value="b">',Matrix2[3])
print('<p id="Q4_2" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r4" id="op15" value="c">',Matrix3[3])
print('<p id="Q4_3" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r4" id="op16" value="d">',Matrix4[3])
print('<p id="Q4_4" style="display:inline"></p></input></br>')     
print('</div>')
print('<div class="container">')
print('<h3>5. </h3>')
print('<p id="p5">',Matrix[4],'</p></br>') 
print('<input type="radio" name="r5" id="op17" value="a">',Matrix1[4])
print('<p id="Q5_1" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r5" id="op18" value="b">',Matrix2[4])
print('<p id="Q5_2" style="display:inline" ></p></input></br>') 
print('<input type="radio" name="r5" id="op19" value="c">',Matrix3[4]) 
print('<p id="Q5_3" style="display:inline"></p></input></br>') 
print('<input type="radio" name="r5" id="op20" value="d">',Matrix4[4])
print('<p id="Q5_4" style="display:inline"></input></br>')
print('</div>')
print('<div class="container">')
print('<h3>6. </h3>')
print('<p id="p6">',Matrix[5],'</p></br>') 
print('<input type="radio" name="r6" id="op21" value="a">',Matrix1[5])
print('<p id="Q6_1" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r6" id="op22" value="b">',Matrix2[5])
print('<p id="Q6_2" style="display:inline"></p></input></br>')    
print('<input type="radio" name="r6" id="op23" value="c">',Matrix3[5])
print('<p id="Q6_3" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r6" id="op24" value="d">',Matrix4[5])
print('<p id="Q6_4" style="display:inline"></p></input></br>')
print('</div>')
print('<div class="container">')
print('<h3>7. </h3>')
print('<p id="p7">',Matrix[6],'</p></br>') 
print('<input type="radio" name="r7" id="op25" value="a">',Matrix1[6])
print('<p id="Q7_1" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r7" id="op26" value="b">',Matrix2[6])
print('<p id="Q7_2" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r7" id="op27" value="c">',Matrix3[6])
print('<p id="Q7_3" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r7" id="op28" value="d">',Matrix4[6])
print('<p id="Q7_4" style="display:inline"></p></input></br>')
print('</div>')
print('<div class="container">')
print('<h3>8. </h3>')
print('<p id="p8">',Matrix[7],'</p></br>') 
print('<input type="radio" name="r8" id="op29" value="a">',Matrix1[7])
print('<p id="Q8_1" style="display:inline"></p></input></br>') 
print('<input type="radio" name="r8" id="op30" value="b">',Matrix2[7])
print('<p id="Q8_2" style="display:inline"></p></input></br>')    
print('<input type="radio" name="r8" id="op31" value="c">',Matrix3[7])
print('<p id="Q8_3" style="display:inline"></p></input></br>')  
print('<input type="radio" name="r8" id="op32" value="d">',Matrix4[7])
print('<p id="Q8_4" style="display:inline"></p></input></br>')     
print('</div>')
print('<div class="container">')
print('<h3>9. </h3>')
print('<p id="p9">',Matrix[8],'</p></br>') 
print('<input type="radio" name="r9" id="op33" value="a">',Matrix1[8])
print('<p id="Q9_1" style="display:inline"></p></input></br>') 
print('<input type="radio" name="r9" id="op34" value="b">',Matrix2[8])
print('<p id="Q9_2" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r9" id="op35" value="c">',Matrix3[8])
print('<p id="Q9_3" style="display:inline"></p></input></br>')    
print('<input type="radio" name="r9" id="op36" value="d">',Matrix4[8])
print('<p id="Q9_4" style="display:inline"></p></input></br>')     
print('</div>')
print('<div class="container">')
print('<h3>10. </h3>')
print('<p id="p10">',Matrix[9],'</p></br>') 
print('<input type="radio" name="r10" id="op37" value="a">',Matrix1[9])
print('<p id="Q10_1" style="display:inline"></p></input></br>') 
print('<input type="radio" name="r10" id="op38" value="b">',Matrix2[9])
print('<p id="Q10_2" style="display:inline"></p></input></br>')   
print('<input type="radio" name="r10" id="op39" value="c">',Matrix3[9])
print('<p id="Q10_3" style="display:inline"></p></input></br>')    
print('<input type="radio" name="r10" id="op40" value="d">',Matrix4[9])
print('<p id="Q10_4" style="display:inline"></p></input></br>')     
print('</div></br></br>')
print('<center>')
print('<input type="button" id="b1" Value="FINISH" Onclick="count()"  style="height:60px;width:120px;font-size:30px"></button>')
print('</center>')
print('</form>')
print('<script>')
print('function count(){')
print('var A,B,C,D,E,F,G,H,I,J,k,m,cntr=0;')
print('var form=document.getElementById("test");')
print('A=form.elements["r1"].value;')
print('B=form.elements["r2"].value;')
print('C=form.elements["r3"].value;')
print('D=form.elements["r4"].value;')
print('E=form.elements["r5"].value;')
print('F=form.elements["r6"].value;')
print('G=form.elements["r7"].value;')
print('H=form.elements["r8"].value;')
print('I=form.elements["r9"].value;')
print('J=form.elements["r10"].value;')
print('var m=document.getElementById("Q1_1").innerHTML;')
print('var str=m.split(",");')
print('var sub=str[0].substr(3,1);')
print('if(A==sub){cntr=cntr+1};')
print('sub=str[1].substr(2,1);')
print('if(B==sub){cntr=cntr+1};')
print('sub=str[2].substr(2,1);')
print('if(C==sub){cntr=cntr+1};')
print('sub=str[3].substr(2,1);')
print('if(D==sub){cntr=cntr+1};')
print('sub=str[4].substr(2,1);')
print('if(E==sub){cntr=cntr+1};')
print('sub=str[5].substr(2,1);')
print('if(F==sub){cntr=cntr+1};')
print('sub=str[6].substr(2,1);')
print('if(G==sub){cntr=cntr+1};')
print('sub=str[7].substr(2,1);')
print('if(H==sub){cntr=cntr+1};')
print('sub=str[8].substr(2,1);')
print('if(I==sub){cntr=cntr+1};')
print('sub=str[9].substr(2,1);')
print('if(J==sub){cntr=cntr+1};')
print('alert("YOU HAVE SCORED "+cntr+" OUT OF 10.");')
print('window.location.href="http://localhost/main.html";')
print('}')
print('</script>')

print('</body>')
print('</html>')