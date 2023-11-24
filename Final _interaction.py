import bpy
import math
import threading
import cv2
import numpy as np
import datetime
import matplotlib.pyplot as plt
import time

camera_lock = threading.Lock()

condition = threading.Condition()

gray = None

def monitor_gray():
    while True:
        with camera_lock:
#            current = bpy.data.scenes['Scene'].frame_current
            if gray is not None and ((np.count_nonzero(gray == 0) / gray.size < 0.87) or (0.5 <= (np.count_nonzero(gray == 0) / gray.size) < 0.9)):
                condition.acquire()  
                condition.notify()  
                condition.release()  
        time.sleep(0.1) 

def camera_thread():
    global gray  
    cap = cv2.VideoCapture(0)  
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1720)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    print("提示：请按q键结束视频保存")

    while True:
        start_time = time.time()  
        ret, frame = cap.read()  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

        thresh = 160
        gray[gray > thresh] = 255
        gray[gray < thresh] = 0
        cv2.imshow('gray', gray)
        
        end_time = time.time()  
        processing_time = end_time - start_time 
        print(f"Image Processing Speed (per frame): {processing_time:.5f} seconds")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  
    cv2.destroyAllWindows()  

decrease = False 
increase_flag = True 

def blender_control_thread():

    target_object_names = ["F1","F2","F3"]  

    GN_name = "GeometryNodes"
    GN_name_2 = "GeometryNodes.001"
    GN_name_3 = "GeometryNodes"
    GN_name_3_1 = "GeometryNodes"
    GN_name_4 = "GeometryNodes"
    GN_name_5 = "GeometryNodes"
    GN_name_C = "GeometryNodes"

    #  F1
    GN_attr_1 = "Input_4"  # 1_Rotation Speed
    GN_attr_2 = "Input_11" # 1_Overll Motion (between-14~14)
    GN_attr_3 = "Input_8"  # 1_Branch Rotation
    GN_attr_4 = "Input_6"  # 1_Leaf Min

    #  F3
    GN_attr_5 = "Input_2"  # 3_Up_Down
    GN_attr_6 = "Input_3"  # 3_Ball Rosition
    GN_attr_7 = "Input_5"  # 3_Swing
    GN_attr_17 = "Input_6"  # 3_ball_size

    #  F3.1
    GN_attr_8 = "Input_2"  # 3-1_UP_DOWN

    #  F2
    GN_attr_9 = "Input_2"  # 2_Breathe
    GN_attr_10 = "Input_5"  # 2_Seeds on size
    GN_attr_11 = "Input_4"  # 2_Roll
    GN_attr_16 = "Input_7"  # Z

    #  F4
    GN_attr_12 = "Input_2"  # 4_Rotation Move
    GN_attr_13 = "Input_3"  # 4_Length

    #  F5
    GN_attr_14 = "Input_2"  # 5_Offest Scale

    # Connection 
    GN_attr_15 = "Input_2"  # Connection_D


    decrease = False  
    direction = True
    
    # 获取场景中的灯光对象
    light_object_2 = bpy.data.objects.get("F2 Light") 
    light_object_3 = bpy.data.objects.get("F3 Light")
    light_object_Right = bpy.data.objects.get("Point_Right")  

    def update(target_object):
        target_object.update_tag()
        bpy.data.scenes['Scene'].frame_current += 1
        
    def update_list(target_list):
        for target_to_update in target_list:
            target_to_update.update_tag()
        bpy.data.scenes['Scene'].frame_current += 1
   
    global sine_wave_upper
    global sine_wave_upper_2    
    global sine_wave_speed
    sine_wave_upper = 0.8  
    sine_wave_upper_2 = 0.7
    sine_wave_speed = 0.05

    def sine_wave(speed, upper_limit, lower_limit):
        global frame_offset
        angle = bpy.data.scenes['Scene'].frame_current
        amplitude = (upper_limit - lower_limit) / 2
        new_value = amplitude * math.sin(angle*speed) + amplitude + lower_limit
        return new_value
    

    def change():
        global sine_wave_upper  
        global sine_wave_upper_2 
        global sine_wave_speed
        
        target_list = []
                
    #________________________________________F1________________________________________________            
            
        target_object = bpy.data.objects.get("F1")
        
    # Interaive_part_______________________________________
    
        with condition:
            if gray is not None and 0.5 <= (np.count_nonzero(gray == 0) / gray.size) < 0.9:
#            if gray is not None and 0.0 <= (np.count_nonzero(gray == 0) / gray.size) < 0.5:
                target_object.modifiers[GN_name][GN_attr_1] = sine_wave(0.01, 0.2, 1) 
                target_object.modifiers[GN_name][GN_attr_2] = sine_wave(0.0006, -12, 12)
                target_object.modifiers[GN_name][GN_attr_4] += 0.1 
            else:
                target_object.modifiers[GN_name][GN_attr_3] = sine_wave(0.03, 0.85, -0.2)

            condition.notify()  
            target_list.append(target_object)  

    #________________________________________F2________________________________________________            
     
        target_object_2 = bpy.data.objects.get("F2")
    
    # Interaive_part_______________________________________
    
        with condition:
            target_object_2.modifiers[GN_name_2][GN_attr_16] = sine_wave(0.08, 0.76, sine_wave_upper_2) 
            if gray is not None and np.count_nonzero(gray == 0) / gray.size < 0.87:                
                sine_wave_upper_2 = min(sine_wave_upper_2 + 0.09, 1.2)    
                target_object_2.modifiers[GN_name_2][GN_attr_9] = sine_wave(0.045, 0.92, 1.14)
                
                light_object_2.data.use_nodes = not light_object_2.data.use_nodes  
                light_object_Right.data.use_nodes = not light_object_Right.data.use_nodes 
                light_object_2.data.energy = 3
                light_object_Right.data.energy = 4   
            else:
                sine_wave_upper_2 = max(sine_wave_upper_2 - 0.06, 0.74)
                target_object_2.modifiers[GN_name_2][GN_attr_11] = sine_wave(0.007, 0.1, 0.11)
                
                light_object_2.data.use_nodes = not light_object_2.data.use_nodes  
                light_object_2.data.energy = 1.5
                light_object_Right.data.use_nodes = not light_object_Right.data.use_nodes 
                light_object_Right.data.energy = 2.58

            condition.notify()  
            target_object_2.modifiers[GN_name_2][GN_attr_10] = sine_wave(0.02, -0.25, 1.3)
            target_list.append(target_object_2)
                
    #________________________________________F3________________________________________________  
              
        target_object_3 = bpy.data.objects.get("F3") 
    
    # Interaive_part_______________________________________ 
    
        with condition:
            target_object_3.modifiers[GN_name_3][GN_attr_5] = sine_wave(sine_wave_speed, 0.3, sine_wave_upper)
            
            if gray is not None and np.count_nonzero(gray == 0) / gray.size < 0.87:
                sine_wave_upper = min(sine_wave_upper + 0.03, 1.2)
                sine_wave_speed = min(sine_wave_speed + 0.001, 0.06)
                
                target_object_3.modifiers[GN_name_3][GN_attr_17] = sine_wave(0.01,0.06,0.06)

                light_object_3.data.use_nodes = not light_object_3.data.use_nodes  
                light_object_3.data.energy = 3  
                        
            else:
                sine_wave_upper = max(sine_wave_upper - 0.03, -0.1)
                sine_wave_speed = max(sine_wave_speed - 0.02, 0.05)
                
                target_object_3.modifiers[GN_name_3][GN_attr_17] = sine_wave(0.05,0.04,0.06)
                
                light_object_3.data.use_nodes = not light_object_3.data.use_nodes  
                light_object_3.data.energy = 1  
                
            condition.notify()  
            target_object_3.modifiers[GN_name_3][GN_attr_6] = sine_wave(0.005, -0.6, 4.5) 
            target_object_3.modifiers[GN_name_3][GN_attr_7] = sine_wave(0.03, -0.1, -0.35) 
      
            target_list.append(target_object_3)

    #________________________________________F3-1________________________________________________            
        
        target_object_3_1 = bpy.data.objects.get("F3.1")      
            
        if target_object_3_1 is not None:
            target_object_3_1.modifiers[GN_name_3_1][GN_attr_8] = sine_wave(0.03, 1.4, 1.6) 

            target_list.append(target_object_3_1)
            
    #__________________________________________F4_________________________________________________            
        
        target_object_4 = bpy.data.objects.get("F4")      
            
        if target_object_4 is not None and 0.5 <= (np.count_nonzero(gray == 0) / gray.size) < 0.9:
    #        target_object_4.modifiers[GN_name_4][GN_attr_12] = sine_wave(0.0005, -20, 20) 
            target_object_4.modifiers[GN_name_4][GN_attr_13] = sine_wave(0.01, -1.5, 1.9)
            target_object_4.modifiers[GN_name_4][GN_attr_12] = sine_wave(0.05, -6, 6)
        else:
            target_object_4.modifiers[GN_name_4][GN_attr_13] = sine_wave(0.005, -1.5, 1.9)
            target_object_4.modifiers[GN_name_4][GN_attr_12] = sine_wave(0.01, -6, 6)    
      
            target_list.append(target_object_4)     
                       
    #________________________________________F5________________________________________________     
        
        target_object_5 = bpy.data.objects.get("F5") 
           
    # Interaive_part_______________________________________    
    
        with condition:
            if gray is not None and np.count_nonzero(gray == 0) / gray.size < 0.87:
                target_object_5.modifiers[GN_name_5][GN_attr_14] = sine_wave(0.05, -0.5, -0.1) 
            else:
                target_object_5.modifiers[GN_name_5][GN_attr_14] = sine_wave(0.05, -0.1, 0.45) 
    
            target_list.append(target_object_5)

    #____________________________________Connection____________________________________________     
         
        target_object_C = bpy.data.objects.get("connection")    
        
        if target_object_C is not None:       
            target_object_C.modifiers[GN_name_C][GN_attr_15] = sine_wave(0.01, -0.5, -0.9)
            
            target_list.append(target_object_C)

#            print(f"target_object.modifiers[GN_name][GN_attr][GN_attr_1]...")
        update_list(target_list)
    #__________________________________________________________________________________________           
            
    def loop(iteration=1500, delay=0.05):
        for i in range(iteration):
            if i < iteration - 1:       
                bpy.app.timers.register(change, first_interval=delay * (i + 1))    

    for target_object_name in target_object_names:  
        target_object = bpy.data.objects.get(target_object_name)
        
    if target_object:
    #    target_object.modifiers[GN_name][GN_attr_1] = 0.1

        update(target_object)    
        loop()
    else:
        print(f"未找到名为 {target_object_name} 的对象")

        
monitor_thread = threading.Thread(target=monitor_gray)
monitor_thread.start()

camera_thread = threading.Thread(target=camera_thread)
camera_thread.start()

blender_control_thread = threading.Thread(target=blender_control_thread)
blender_control_thread.start()