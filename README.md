# Ecological_Resonance
### Note: 
To run the script within the Blender file, it is necessary to establish a TCP server and import OpenCV.  
### Video Link: 
## WEEK0
在前期部分对于毕设主题内容进行了反复的调整，尝试了多个主题。和导师多次共同后选定_Ecological_Resonance_作为最终毕设内容。
## WEEK1
This week is primarily focused on establishing the background, theme, content, and form of the artwork.
### Inspiration  
如今的生态问题人与生物和谐共存的环境会是什么样子的？我们该如何想象未来环境？  
The inspiration  
因为主题背景，使用blender几何节点建模非常符合我的需求。同时也发现了如今的一些关于几何节点建模在实时交互的应用的弊端。  
### Background
 "Ecological Resonance" provides a glimpse into the potential past under the development of data and information in the future. In this futuristic scenario, the form of living organisms is considered an event within time and space. To adapt to digital development, organisms in the city construct an evolving lineage over time, with urban crevices becoming new living spaces for these digitally predefined "organisms." 
 

### About Work  
Through a process that resembles archaeological discovery, people can directly intervene in the exhibition space: gaining access to the hidden digital ecosystems beneath the city, while also altering the products of growth and evolution dependent on data. Human activities activate the experience of time and reveal the changing existence over time.  

 _Ecological Resonance_ does not attempt to provide a definite answer to what the future should be. Instead, it strives to promote a spiritual ecology where participants can more effectively raise and discuss these questions. It encourages contemplating the potential impact of human digital traces on the living organisms from speculative and dialectical perspectives.  

When everything achieves harmony, people standing in the real space will discover their integration into the unfolding world before them.

![草图](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/ef9f5775-9bef-4361-adf0-431f0527d710)


## WEEK2
This week is 
生物模型设计：我在生物形态设计中引入了线条这一设计元素。选择线条的原因在于其具有传递与连接数据的含义。线条与生物柔软的结构相结合，不仅在视觉上表达了生物的感性特质，还体现了数据的理性属性。线条不仅存在于个体生物内部，同时还贯穿于多个生物体之间，形成相互作用的关联。
![建模过程](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/e95a920f-fb30-4042-83f1-6421c0f47c0f)
进行了大量的几何节点建模工作，在工作中，"Instance on Points" 模块是我广泛应用的一个模块。该模块以一种高度灵活的方式支持复杂模型的创建。因此，我能够利用该模块持续叠加元素于生物结构中，从而丰富生物的视觉呈现。  
为模拟自然随机性的效果，我还广泛应用了“Noise Texture”、“Wave Texture”等纹理模块。这些模块的使用进一步增强了模型的真实感和视觉吸引力。最终各部分结构可以实现自然的摇摆，伸缩，旋转等运动方式。  

## WEEK3
This week is 
贴图，渲染。发现了Eevee渲染
![E--EC](https://github.com/YirenWA/Final_Project-Ecological_Resonance/assets/119879041/3c313e69-dd18-47ce-8cc4-6f31e5fc0899)
控制运动形态的节点选择
## WEEK4
### Control Target Objects propor
This week is 
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
