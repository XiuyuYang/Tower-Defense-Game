# Tower-Defense-Game

I want to make a tower defense game, the first step is to create a map, I want to make a map editor for the player to use in order to generate maps.

![GIF 2023-1-24 22-23-33](https://user-images.githubusercontent.com/54026897/214255222-d2f0cf8a-d465-47f8-a15b-95473f5331b6.gif)

25/01/2023
I make a cell with corner numbers so I can find correct mesh with different hightness in the future.

![image](https://user-images.githubusercontent.com/54026897/214275808-93520ad0-b793-4f1e-b93b-32abc0adc33e.png)

![GIF 2023-1-25 0-00-15](https://user-images.githubusercontent.com/54026897/214275031-7a74c11b-f90c-4ed7-97ce-5e2e7a8d1a2d.gif)

29/01/2023

I calculated that if the maximum span height per unit of terrain was 4 levels, I could represent the height of the vertices as a quadrilimal number (i.e. 0000-3333), with 256 height combinations. If I reduce the number of assemblies I need to make using only rotation or up and down displacement [replacing geometry of height (1111) with (0000)], I can reduce the total number to 46.
I used two datatable methods to query the aggregate, the first datatable storing the heights and corresponding geometry of the four corners of the aggregate. The second datatable stores information about how many degrees of rotation each of the 46 geometers corresponding to all the different height combinations has been made. The second list is actually 175 instead of 256, because it removes all items that do not contain 0 height. In theory, any geometry that does not contain 0 and each vertex is no more than 3 in height can be matched in the existing entries by moving up and down.

![image](https://user-images.githubusercontent.com/54026897/215318023-f1701402-7fa9-4799-9166-75bb65ff9b3a.png)

![image](https://user-images.githubusercontent.com/54026897/215318057-9088894f-52a5-4788-9058-77fa0998b6f9.png)

![GIF 2023-1-29 22-17-25](https://user-images.githubusercontent.com/54026897/215316975-1e6a0e44-2e2c-4684-8f5d-a23ea5823a42.gif)
