# christmas_message_remastered
Christmas message plus some Christmas Tree

## How does it work? ❓
Ok, first create the instance of the class

After that, do:
```py
christmas_tree = ChristMasTree(add_star=True) #It adds a little start in the top. However you can remove it or set it to False if you don't want it
christmas_tree.display('Merry Christmas', 'EVERYONE', light_perimeter=True, rand_color=True)
```
Ok, first parameter is the message and the second is the destination, 
to whoever you are going to send this little simple gift.
`light_perimeter` basically fills with yellow in the perimeter while `rand_color` just fills the area with random colors (READ THE DOC OF THE FUNCTION)

### ⚠️ Little Warning
Setting `light_perimeter` and rand_color to True, the available colors will be:
`BLUE` and `GREEN` otherwise if light_perimeter is False random colors are: `BLUE`, `GREEN` and `CYAN`.
Don't need to fix it, this is how i intended to do it.

#### light_perimeter to True 
![Captura de pantalla 2021-12-26 a las 12 54 36 p  m](https://user-images.githubusercontent.com/89955811/147412630-76f6d56e-def4-48d0-b121-baa109fbb967.png)

#### light_perimeter to False
![Captura de pantalla 2021-12-26 a las 1 37 45 p  m](https://user-images.githubusercontent.com/89955811/147413046-a5050ea6-624f-4ce9-9fab-0f036ec6f76b.png)


## Contribution 🛠️
You need my permission first to change something in here.







