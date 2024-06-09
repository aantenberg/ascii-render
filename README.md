# ASCII 3D Renderer
This is a simple ASCII 3D renderer that can create scenes with a single point light.
Objects can be added to the scene, and lambertian shading is used to render the scene
in the terminal.

For example, the following is a simple render generated of a scene with a sphere and a point light:

**With console in dark mode:**
```
                  ! * ! ; , .                                   
              @ @ @ @ @ @ * ; . .                               
          0 @ @ @ @ @ @ @ @ * : . . .                           
        0 @ @ @ @ @ @ @ @ @ @ < , . . .                         
        @ @ @ @ @ @ @ @ @ @ @ ! - . . .                         
      @ @ @ @ @ @ @ @ @ @ @ @ ! : . . . .                       
      @ @ @ @ @ @ @ @ @ @ @ @ ! - . . . .                       
    ! @ @ @ @ @ @ @ @ @ @ @ 0 < - . . . . .                     
    * @ @ @ @ @ @ @ @ @ @ @ * ; , . . . . .                     
    ! @ @ @ @ @ @ @ @ @ @ 0 < - . . . . . .                     
    ; @ @ @ @ @ @ @ @ @ @ ! : , . . . . . .                     
    , * @ @ @ @ @ @ @ 0 ! ; , . . . . . . .                     
    . ; * @ @ @ @ 0 * < : , . . . . . . . .                     
      . : < ! ! ! < ; - , . . . . . . . .                       
      . . , - : - - , . . . . . . . . . .                       
        . . . . . . . . . . . . . . . .                         
        . . . . . . . . . . . . . . . .                         
          . . . . . . . . . . . . . .                           
              . . . . . . . . . .                               
                  . . . . . .                                                                                       
```

**With console in light mode:**
```
                  : - : < 0 @                                   
              . . . . . . - < @ @                               
          , . . . . . . . . - ! @ @ @                           
        , . . . . . . . . . . ; 0 @ @ @                         
        . . . . . . . . . . . : * @ @ @                         
      . . . . . . . . . . . . : ! @ @ @ @                       
      . . . . . . . . . . . . : * @ @ @ @                       
    : . . . . . . . . . . . , ; * @ @ @ @ @                     
    - . . . . . . . . . . . - < 0 @ @ @ @ @                     
    : . . . . . . . . . . , ; * @ @ @ @ @ @                     
    < . . . . . . . . . . : ! 0 @ @ @ @ @ @                     
    0 - . . . . . . . , : < 0 @ @ @ @ @ @ @                     
    @ < - . . . . , - ; ! 0 @ @ @ @ @ @ @ @                     
      @ ! ; : : : ; < * 0 @ @ @ @ @ @ @ @                       
      @ @ 0 * ! * * 0 @ @ @ @ @ @ @ @ @ @                       
        @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @                         
        @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @                         
          @ @ @ @ @ @ @ @ @ @ @ @ @ @                           
              @ @ @ @ @ @ @ @ @ @                               
                  @ @ @ @ @ @  
```

The renderer is optimized for dark-mode interfaces, with a dark background and white text, but can also be
used in light mode through constructor parameters.
