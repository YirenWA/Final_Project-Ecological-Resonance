# Ecological_Resonance
Note: It is necessary to establish a TCP server and import OpenCV to run the script within the Blender file.  
### Video Link: https://youtu.be/UEF9MdYHU90

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

## WEEK3
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

## WEEK4
This week is 
### Control the properties of the target object(s)
最开始通过插件Alter mesh将几何节点模型及其节点输入端口导入Unreal Engine。然而通过实验发现，支持其参数更改的模型类型不支持实时交互窗口的应用。
所以我尝试从Blender软件本身寻找突破。使用Blender Python API来访问程序的内部可以极大地扩展Blender几何节点的交互功能。所以在Blender中通过TCP连接与其他应用程序通信可以实现数据传输和交换，
使用bpy，在脚本内控制几何节点输入端口  

比较了“不断增加或减小常数值”和“正弦函数”两者在改变生物运动节点参数上的视觉效果。在项目实践中发现，使用正弦函数具有平滑过渡，可预测性和灵活性的优势。它更加适用于需要模拟自然或有机运动的场景。我定义了正弦波函数，应用的函数接收三个参数：speed（速度）、upper_limit（波形的上限值）和lower_limit（波形的下限值）。根据当前场景的帧数，计算正弦波的值以模拟周期性的变化。并将计算结果在给定的上限和下限之间。
![sine_wave](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/8fda3c59-73e5-42ea-b5a1-ee7139a945e3)
定义的sine函数
![sine wave应用](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/e6be9b8c-1dbe-48db-a6ba-1aa7ff353cf5)
sine函数的应用

## WEEK5
### OpenCV
This week is 
先在python内进行OpenCV对图像灰度化和二值化的处理，然后再将这部分内容添加到blender的脚本内。（import OpenCV库）
![opencv](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/3885077d-b361-4483-a371-4d25ccb1d01c)

## WEEK6
多线程设计
![Process3_bpy_input node_2](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/0a72e0d2-cfc3-4e0d-9273-949af368a480)
小的沙子覆盖测试

## WEEK7
This week is 主要是在装置场景搭建设计
To create an immersive experience, I made a sand model to simulate urban crevices. 同时是围栏，也可以限制沙子不会跑出范围。
![场景搭建](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/43834317-9658-4b03-a09d-ed7f7a9b4fdf)
为了贴合显示屏的曲面，将它稳固在位置上，做了一个支撑。  
![支撑](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/fd13e11d-c9f0-425d-bcd3-c7861b02820b)

## WEEK8
### Test  
将所有内容整合到一起，进行测试
### Result
