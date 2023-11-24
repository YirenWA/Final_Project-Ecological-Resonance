# Ecological_Resonance
Note: It is necessary to establish a TCP server and import OpenCV to run the script within the Blender file.  
### Video Link: 
https://youtu.be/UEF9MdYHU90

## WEEK 0
The preliminary work involved repeatedly adjusting the theme of the Final project. After numerous discussions with my supervisor, we finally chose _Ecological Resonance_ as the final topic.  

## WEEK 1
This week is primarily focused on establishing the background, theme, content, and form of the artwork.
### Inspiration  
What would a future environment where humans and organisms coexist harmoniously look like?   
How do we imagine the future environment?    

![1](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/5f414d82-9174-4aae-aab0-f481004a9250)

### Background
_Ecological Resonance_ provides a glimpse into the potential past under the development of data and information in the future. In this futuristic scenario, the form of living organisms is considered an event within time and space. To adapt to digital development, organisms in the city construct an evolving lineage over time, with urban crevices becoming new living spaces for these digitally predefined "organisms."   

Due to the artistic background set, using Blender's geometry node modeling fits well with my needs for designing predefined digital organisms. At the same time, I also discovered the current limitations of geometry node modeling in real-time interactive applications. 

### About Work  
Achieving the technical goal of using Blender's geometry node ports as input objects for touchless real-time interaction also meant realizing _Ecological Resonance_ interactive installation.  

Through a process that resembles archaeological discovery, people can directly intervene in the exhibition space: gaining access to the hidden digital ecosystems beneath the city, while also altering the products of growth and evolution dependent on data. Human activities activate the experience of time and reveal the changing existence over time. I made a preliminary design for the structure of the installation. People excavated and exposed hidden organisms, a process that also changed the surrounding environment. The change in environment by humans impacts the organisms' habitat, causing them to continuously adapt to these changes and evolve.  

![草图](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/ef9f5775-9bef-4361-adf0-431f0527d710)

_Ecological Resonance_ does not attempt to provide a definite answer to what the future should be. Instead, it strives to promote a spiritual ecology where participants can more effectively raise and discuss these questions. It encourages contemplating the potential impact of human digital traces on the living organisms from speculative and dialectical perspectives. When everything achieves harmony, people standing in the real space will discover their integration into the unfolding world before them.  

## WEEK 2
This week, based on the work from the previous week, I began the specific design process. I started by using Blender's geometry nodes to construct various organisms' models.   

### Modeling Design of Organisms
In my design of organism morphology, I introduced lines as a design element. The reason for choosing lines is that they have the meaning of transmitting and connecting data. When combined with the soft structure of organisms, lines not only visually express the sensual characteristics of organisms, but also reflect the rational attributes of data.   

![2](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/8d97bd0c-e4c3-4104-904b-a1b9b059a953)

![建模过程](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/e95a920f-fb30-4042-83f1-6421c0f47c0f) 

Subsequently, I engaged in extensive geometry node modeling work. In the process, "Instance on Points" module is one that I extensively utilized. This module supports the creation of complex models in a highly flexible manner. Thus, I could continually stack elements within the organism structure using this module, thereby enriching the visual presentation of the organism.   

![GN](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/b9066537-9176-4164-9303-75e5be6dea92)

To simulate the effects of natural randomness, I also extensively used Texture modules like "Noise Texture" and "Wave Texture." The utilization of these modules further enhanced the realism and visual appeal of the models. Eventually, various parts of the structure could achieve natural movements such as swaying, stretching, and rotating.   

## WEEK 3
The main focus of this week's work was to lay the foundation for the models within Blender to participate in real-time rendering. 
### Rendering
In the initial design, I consistently worked on shader editing of materials under the Cycles rendering engine. However, to ensure smoothness in real-time interaction, I have to choose Eevee as the rendering engine. Eevee prioritizes rapid rendering and interactive experiences, capable of generating quick previews in a short time. But at this point I realised that Eevee does not entirely trace ray paths, resulting in some limitations in achieving lifelike visuals and lighting accuracy. This results in a much less visually effective scene.   

![E--C](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/5f77f62d-7ff3-4420-a95c-d8907c8b057b)

So I conducted a series of optimization experiments to solve the problem:   
To start, I activated the Ambient Occlusion feature in the Eevee rendering engine. This feature is commonly used to simulate the effect of light obstruction in recessed areas, thereby enhancing the rendering quality. Simultaneously, I incorporated the Ambient Occlusion module into the Shader Editor of the model's materials to accentuate the lighting and shadows in the recessed areas, enhancing the scene's details and realism. This method proves more convenient and effective compared to creating soft shadows using an array of lights.  

![AO—](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/0bfa5a14-3472-4164-bcaf-8f1a136ecb13)

I also adjusted like applying textures to the material's Displacement output and reducing subsurface scattering in materials. The comparison of Eevee rendering effects before and after adjustments is shown below.  

![E--EC](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/3c313e69-dd18-47ce-8cc4-6f31e5fc0899)

### Geometric Node Selection
Finally, for different organisms, I selected nodes that would change their forms. These were then added to the Group Input for convenient direct control of node parameters later on.    

![节点选择](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/bcc8ce98-c474-4c26-9261-7713636f96f1)
An example of node selection for one model.  

## WEEK 4
### Control the properties of the target object(s)
To make the previous work realize Interactive 3D, I imported the geometry node models and their node input ports into Unreal Engine using the Alter mesh plugin. However, experiments revealed that the model types supporting parameter changes did not support applications of real-time interactive windows.  

Therefore, I attempted to find a breakthrough from within Blender software itself. Using the Blender Python API to access the program's internals significantly expanded the interactive capabilities of Blender's geometry nodes. Communication with other applications via TCP connection within Blender enabled data transmission and exchange. Finally, I used bpy in the Blender script to specify and control the geometry node input ports.  
I went from controlling a single model to controlling multiple models through scripts with the following design flow:  

![control_1 to 3-01_画板 1_画板 1](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/94f0937d-93be-4ad3-89bb-5b8ea9c9472e)

In the case of controlling a single object:  
1.	Specify the target object: Clearly define the geometry node object and its input ports.   
2.	Define the update function: Ensure that changes in the scene progress by one frame with every function call.  
3.	Define the change function: Used to alter the specified object's attributes. When conditions are met, execute the corresponding modification operations.   
4.	Define the loop function: Create a timer that triggers the change function at a certain time interval. This operation achieves the cyclic iteration of the organism movement.   

When transitioning from controlling a single object to controlling multiple objects, with an increase in the number of models, I defined the “update list (target list)” function after defining the update function. This function is used to update a batch of objects passed in a list, executing update operations for each object in the list. This batch update method can improve efficiency and ensure that multiple incoming objects are all updated to the latest state.  

### Calculate the Properties' Values of the Target Object
I found that the initial method of "continuously increasing or decreasing a constant value" caused the motion of the organisms model to stutter. In the project practice, I observed that using a sine function offers the advantages of smooth transitions, predictability, and flexibility. Therefore, I adopted the "sine function" to calculate the properties' values of target objects. The sine function is suitable for scenarios requiring simulation of natural or organic motion. I defined the ‘sine_wave’ function and the applied ‘sine_wave’ function accepted three parameters: ‘speed’, ‘upper_limit’, and ‘lower_limit’. Based on the current scene's frame rate, it calculated the sine wave's value to simulate periodic changes and limited the computed result within the provided upper and lower limits.   

![sine_wave](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/8fda3c59-73e5-42ea-b5a1-ee7139a945e3)

![sine wave应用](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/e6be9b8c-1dbe-48db-a6ba-1aa7ff353cf5)
Example of the sine_wave function used for calculations.   

## WEEK 5
This week, the focus was primarily on researching OpenCV based on the Python language, and organizing the framework of the thesis.   

### OpenCV
I utilized OpenCV's image processing to implement the content of the touchless interactive system in the artwork. First, the camera images were processed for grayscale and binarization within Python using OpenCV, and then this content was integrated into the Blender script. OpenCV libraries were introduced within Blender. 

![opencv](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/3885077d-b361-4483-a371-4d25ccb1d01c)  

![结构图](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/218dd313-431f-4b62-ab52-4b7589b5edda)

Depending on the structure of the installation. The camera images undergo grayscale and binarization processing. This method represents sand as black pixels and the bright monitor below as white pixels. Through this approach, it becomes possible to calculate information about the sand's coverage area in the frame. 

![opencv 图像处理 ](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/9253d838-fdea-43db-9a18-b17916162f77)

## WEEK 6
This week's work primarily involved using real-time data from the OpenCV camera to control the changes in Geometry Node parameters within Blender.    

I found the limitations of single-threaded execution make it infeasible to simultaneously preview both the real-time rendering window and the OpenCV camera window. Therefore, I adopted a multi-threaded solution to concurrently run and manage these two functions.   

### Multi-Threaded Design
1.	The first thread is the Camera Thread. It utilizes the OpenCV library to capture real-time images from the camera  process the images.  

![gray_2](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/39686d68-5b98-4bc2-823f-3f2a0d2bf7bd)

2.	The second thread is the Blender Control Thread. It integrates the work of the target object's geometry node properties developed. When specific conditions are met, this thread is responsible for updating these properties, thus enabling dynamic effects on the target objects.   

![gray_3](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/316cd51a-00ac-43a0-8d56-d2cf5c43ccdf)

3.	The third thread is the Monitor Thread. It continuously monitors the proportion of black and white pixels in the grayscale image. When specific conditions are met, it triggers other threads to execute corresponding operations. Condition locks and notification mechanisms are utilized here to ensure synchronization between threads.  

![gray_4](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/8b0d2238-179b-4189-b9ab-30064dc29302)

By creating and starting the three threads, the entire interactive process can be successfully implemented.  

### Small Test  

After implementing the above content, I conducted a identification and triggering test using a small screen and the coverage of sand.  

![小测试](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/01d911e0-abd9-4721-a4eb-05978b71dc92)

![Process3_bpy_input node_2](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/0a72e0d2-cfc3-4e0d-9273-949af368a480) 


## WEEK 7
本周主要是在制作装置的各部分内容。
To create an immersive experience, I made a sand model to simulate urban crevices. 同时它也可以限制沙子不会跑出范围。
![场景搭建](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/43834317-9658-4b03-a09d-ed7f7a9b4fdf)
为了贴合显示屏的曲面，并将它稳固在较低的位置上，我制作了一个支撑。  
![支撑](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/fd13e11d-c9f0-425d-bcd3-c7861b02820b)

## WEEK8
### Test  
最终前几周的工作整合到一起，进行了测试。根据精准度的测试，我还对代码进行了调整。

![图表_画板 1](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/500a1485-fbc4-4425-be3d-2c7f1ac5e472)
To improve interaction accuracy, I further adjusted the sand coverage conditions and control code content using an overlapping cross method to ensure a closer coordination between the two. This involved introducing more conditions within the sand coverage conditions.   

### 视频拍摄剪辑


### Result
