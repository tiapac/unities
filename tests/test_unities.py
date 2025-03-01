

if __name__ == "__main__":
    import unities as u 
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    
    cm       = u.symbols("cm")
    g        = u.symbols("g")
    s        = u.symbols("s")
    velocity = cm*(s**-1)
    force    = u.symbols("dyne")#,  subsymbols= {g, cm,s**-2})
    pressure = force*(cm**-2)
    
    foo = pressure*velocity
    # print("".join(["%s %s\n"%(type(x), x) for x in [cm, g, s, vel, force, pressure, foo, fluxx]]))
    
    v1 = u.quantity((1, velocity))
    v2 = u.quantity((40, velocity))
    
    sts = v1*10.
    sts = v2/4. 
    sts = v2**-1
    sts = v2**2 
    sts = v1*v2 
    sts = v1*cm 

    
    pltArgs  = dict(fontsize=12, ha='center')

    with PdfPages('symbols.pdf') as pdf:
        fig, ax = plt.subplots()
        ax.text(0.1, 0.8, f"This is the CGS system, in ${cm}$, ${g}$ and ${s}$!" )
        ax.text(0.1, 0.7, f"Test implicit multiplication: \n${velocity}$"     )
        ax.text(0.1, 0.6, f"Test explicity multiplication:\n${cm*(s**(-1))}$" )
        ax.text(0.1, 0.5, f"Test division  operand       :\n${cm/s}$"         )
        ax.text(0.1, 0.4, f"Test power of negative number:\n${cm**(-2)}$"     )
        ax.text(0.1, 0.3, f"Test power of positive number:\n${velocity**2}$"  )
        ax.text(0.1, 0.2, f"Force units is ${force}$"   )
        ax.text(0.1, 0.1, f"Foo is ${foo}$"   )
        
        ax.text(0.7, 0.9, f"This is a number, with a value \n and a unit:  ${velocity}$" )
        ax.text(0.7, 0.8, f"but also:  ${v1}$" )
        ax.text(0.7, 0.7, f"and also:  ${v2}$" )
        ax.text(0.7, 0.6, f"multiply by 10\n ${v1*10.}$")
        ax.text(0.7, 0.5, f"divide with slash\n ${v2/4.} $")
        ax.text(0.7, 0.4, f"test power of negative number:\n ${v2**-1}$")
        ax.text(0.7, 0.3, f"test power of positive number:\n ${v2**2} $")
        ax.text(0.7, 0.2, f"test multiplication ${v1*v2} $")
        ax.text(0.7, 0.1, f"test multiplocation with just unit ${v1*cm} $")

        
        ax.axis('off')
        #pdf.savefig(fig)
        plt.show()
    plt.close()
