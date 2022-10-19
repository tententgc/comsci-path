def func(x):
    return x**3 - 3*x + 1


"""ในการวิเคราะห์เชิงตัวเลข , วิธีการของนิวตันยังเป็นที่รู้จักในฐานะNewton-Raphson วิธีการตั้งชื่อตามไอแซกนิวตันและโจเซฟราฟสันเป็นอัลกอริทึมรากหาซึ่งเป็นผู้ผลิตที่ดีขึ้นอย่างต่อเนื่องใกล้เคียงกับราก (หรือเลขศูนย์) ของจริง -valued ฟังก์ชั่น เวอร์ชันพื้นฐานที่สุดเริ่มต้นด้วยฟังก์ชันตัวแปรเดียวf ที่กำหนดสำหรับตัวแปรจริง xอนุพันธ์ ของฟังก์ชันf ′และการเดาเริ่มต้นx 0สำหรับรูทของฉ . หากฟังก์ชันเป็นไปตามสมมติฐานที่เพียงพอและการคาดเดาเริ่มต้นใกล้เคียงแล้ว"""
# Derivative of the above function
# which is 3*x^x - 2*x


def derivFunc(x):
    return 3*x**2 - 3
# Function to find the root


def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ",
          "%.4f" % x)


# Driver program to test above
x0 = 1.1  # Initial values assumed
newtonRaphson(x0)
