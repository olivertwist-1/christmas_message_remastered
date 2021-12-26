# christmas_message_remastered
Christmas message plus some Christmas Tree

![Captura de pantalla 2021-12-26 a las 12 54 36 p  m](https://user-images.githubusercontent.com/89955811/147412630-76f6d56e-def4-48d0-b121-baa109fbb967.png)

## How does it work? ❓
Ok, first create the instance of the class

After that, do:
```py
christmas_tree = ChristMasTree(add_star=True) #It adds a little start in the top. However you can remove it or set it to False if you don't want it
christmas_tree.display('Merry Christmas', 'EVERYONE', light_perimeter=True, rand_color=True)
```
Ok, first parameter is the message and the second is the destination.
To whoever you are going to send this little simple gift.
`light_perimeter` basically fills with yellow in the perimeter while `rand_color` just fills the area with random colors (READ THE DOC OF THE FUNCTION)

### ⚠️ Little Warning
Setting `light_parameter` and rand_color to True, the available colors will be:
`BLUE` and `GREEN` otherwise if light_paramter is False random colors are: `BLUE`, `GREEN` and `CYAN`.
Don't need to fix it, this is how i intended to do it.

## Contribution 🛠️
Don't feel free to contribute here unless you've got my permission.






