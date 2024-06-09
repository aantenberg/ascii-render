# ASCII 3D Renderer
This is a simple ASCII 3D renderer that can create scenes with a single point light.
Objects can be added to the scene, and lambertian shading is used to render the scene
in the terminal.

## Basic Rendering
For example, the following is a simple render generated of a scene with a sphere and a point light:
**With console in dark mode:**
```
                           .  ,  ,  ,  .  .                                                   
                     -  :  ;  ;  :  :  -  ,  .  .                                             
               .  :  ;  <  !  !  <  <  ;  :  -  .  .  .                                       
            .  :  <  !  *  *  *  *  !  <  ;  :  -  .  .  .                                    
            :  <  *  0  0  0  0  0  *  !  <  ;  -  ,  .  .                                    
         -  ;  !  0  0  @  @  @  0  *  !  <  ;  :  ,  .  .  .                                 
         :  <  *  0  @  @  @  @  0  0  *  !  ;  :  -  .  .  .                                 
      .  ;  !  *  0  @  @  @  @  0  0  *  !  ;  :  -  .  .  .  .                              
      ,  ;  !  *  0  @  @  @  @  0  *  !  <  ;  :  -  .  .  .  .                              
      ,  :  <  *  0  0  0  0  0  0  *  !  <  ;  :  ,  .  .  .  .                              
      ,  :  <  !  *  *  0  0  *  *  !  <  ;  :  -  ,  .  .  .  .                              
      .  -  ;  <  !  !  *  *  !  !  <  ;  ;  :  -  ,  .  .  .  .                              
      .  ,  :  ;  <  <  !  !  <  <  ;  ;  :  -  ,  .  .  .  .  .                              
         .  -  :  ;  ;  ;  ;  ;  ;  :  :  -  ,  .  .  .  .  .                                 
         .  .  -  -  :  :  :  :  :  -  -  ,  .  .  .  .  .  .                                 
            .  .  ,  ,  -  -  -  ,  ,  ,  .  .  .  .  .  .                                    
            .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .                                    
               .  .  .  .  .  .  .  .  .  .  .  .  .  .                                       
                     .  .  .  .  .  .  .  .  .  .                                             
                           .  .  .  .  .  .
```

**With console in light mode:**
```
                           @  0  0  0  @  @                                                   
                     *  !  <  <  !  !  *  0  @  @                                             
               @  !  <  ;  :  :  ;  ;  <  !  *  @  @  @                                       
            @  !  ;  :  -  -  -  -  :  ;  <  !  *  @  @  @                                    
            !  ;  -  ,  ,  ,  ,  ,  -  :  ;  <  *  0  @  @                                    
         *  <  :  ,  ,  .  .  .  ,  -  :  ;  <  !  0  @  @  @                                 
         !  ;  -  ,  .  .  .  .  ,  ,  -  :  <  !  *  @  @  @                                 
      @  <  :  -  ,  .  .  .  .  ,  ,  -  :  <  !  *  @  @  @  @                              
      0  <  :  -  ,  .  .  .  .  ,  -  :  ;  <  !  *  @  @  @  @                              
      0  !  ;  -  ,  ,  ,  ,  ,  ,  -  :  ;  <  !  0  @  @  @  @                              
      0  !  ;  :  -  -  ,  ,  -  -  :  ;  <  !  *  0  @  @  @  @                              
      @  *  <  ;  :  :  -  -  :  :  ;  <  <  !  *  0  @  @  @  @                              
      @  0  !  <  ;  ;  :  :  ;  ;  <  <  !  *  0  @  @  @  @  @                              
         @  *  !  <  <  <  <  <  <  !  !  *  0  @  @  @  @  @                                 
         @  @  *  *  !  !  !  !  !  *  *  0  @  @  @  @  @  @                                 
            @  @  0  0  *  *  *  0  0  0  @  @  @  @  @  @                                    
            @  @  @  @  @  @  @  @  @  @  @  @  @  @  @  @                                    
               @  @  @  @  @  @  @  @  @  @  @  @  @  @                                       
                     @  @  @  @  @  @  @  @  @  @                                             
                           @  @  @  @  @  @
```

The renderer is optimized for dark-mode interfaces, with a dark background and white text, but can also be
used in light mode through constructor parameters.

## Animation
There is also a simple animation engine, that takes in a scene generator, and renders each frame
at a desired frame rate. The following is an animated physics simulation using the animation engine:

https://github.com/aantenberg/ascii-render/assets/89103525/2227d6a2-6aa5-417f-a50c-521ee7bce757

Feel free to run this demo yourself by running `main.py`!
