# ASCII 3D Renderer
This is a simple ASCII 3D renderer that can create scenes with a single point light.
Objects can be added to the scene, and lambertian shading is used to render the scene
in the terminal.

## Basic Rendering
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

## Animation
There is also a simple animation engine, that takes in a scene generator, and renders each frame
at a desired frame rate. The following are animations created using this engine:

### Bouncing Ball
https://github.com/aantenberg/ascii-render/assets/89103525/2227d6a2-6aa5-417f-a50c-521ee7bce757

### Moving Light
https://github.com/aantenberg/ascii-render/assets/89103525/87cf8f26-fb11-4229-a651-aae2ca718834

Feel free to run thes demos yourself using `main.py`!
