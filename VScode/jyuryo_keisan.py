import numpy as np
from stl import mesh

def tkiness_fixed():
    print('厚さを固定しますか？\n0.いいえ\nはいの場合は厚さを記入->mm')
    input_tf = int(input())
    return 

def material_table():
    m1 = 'アクリル'
    m2 = 'PLA'
    mate = [m1,m2]
    return mate

def material_select():
    print('材料はなににしますか？')
    s_mate = material_table()
    m1,m2 = s_mate
    print('1.',m1,'\n2.',m2)
    input_mateNum = int(input())
    return input_mateNum

def material_specific_gravity_table():
    acrylic_specific_gravity = 1.1
    PLA_specific_gravity = 1.24
    mate_spe_gra_table = [acrylic_specific_gravity,PLA_specific_gravity]
    return mate_spe_gra_table

def acrylic_size():
    print('面積は->')
    menseki = int(input())

def main():
    input_mateNum = material_select() 

    if input_mateNum == 1:
        input_tf =tkiness_fixed()
        if input_tf != 0:
            menseki = acrylic_size()
            tkiness = tkiness_fixed.input_tf
            jyuryou = menseki * 1.1*0.001 *tkiness #g/cm^3
            print(jyuryou,'g')
        else :
            menseki = acrylic_size()
            print('厚さは？')
            tkiness = int(input())
            jyuryou = menseki * 1.1*0.001 *tkiness #g/cm^3
            print(jyuryou,'g')
    
    elif input_mateNum == 2:
        print("stlファイルがありますか?\nYes->1\nNo->2\nplease input Number")
        stl_YorN = int(input())
        if stl_YorN == 1:
            print('stlのデータ 読み込み') 
            #stl_date_name = input()
            #stl_date_name = stl_date_name + ".stl"
            stl_date = mesh.Mesh.from_file('body1.stl')
            volume, cog, inertia = stl_date.get_mass_properties()
            mate_weight = volume * 1.24*0.001
            print(mate_weight,'g')



if __name__ == "__main__":
    main()
    

"""
if tkiness != 0:
    while True:
        print('面積は->   (単位はmm^2)')
        menseki = int(input())
        #print('厚さは-> (単位はmm)')
        #t = int(input())
        print('材質を選んでね\n')
        print('1,アクリル')
        print('10,end')

        inputNum = int(input())
        if inputNum == 1:
            jyuryou = menseki * 1.1*0.001 *tkiness #g/cm^3
            print(jyuryou,'g')

        else :
            print('end')
            break
elif tkiness == 0:
    while True:
        print('面積は->   (単位はmm^2)')
        menseki = int(input())
        print('厚さは-> (単位はmm)')
        t = int(input())
        print('材質を選んでね\n')
        print('1,アクリル')
        print('10,end')

        inputNum = int(input())
        if inputNum == 1:
            jyuryou = menseki * 1.1*0.001 *t #g/cm^3
            print(jyuryou,'g')

        else :
            print('end')
            break
"""