def get_coloring(fig_name):
    
    if fig_name=='fig1a':
        def get_color(method, i):
            if method=="clip":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="nd":
                if i in []:
                    return "orange"
                elif i in [0]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_b":
                if i in []:
                    return "orange"
                elif i in [0, 3]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_ood":
                if i in []:
                    return "orange"
                elif i in [0, 3]:
                    return "red"
                else:
                    return "green"
    
    elif fig_name=="fig1b":
        def get_color(method, i):
            if method=="clip":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="nd":
                if i in [0, 1]:
                    return "orange"
                elif i in [2]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_b":
                if i in [2]:
                    return "orange"
                elif i in [0, 1]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_ood":
                if i in [1]:
                    return "orange"
                elif i in [0, 2, 3]:
                    return "red"
                else:
                    return "green"
    
    elif fig_name == 'fig6a':           
        def get_color(method, i):
            if method=="clip":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="nd":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="milan_b":
                if i in [0, 5]:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="milan_ood":
                if i in [0, 1, 3, 5, 6]:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
    
    elif fig_name == 'fig6b':
        def get_color(method, i):
            if method=="clip":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="nd":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="milan_b":
                if i in [0, 3, 5]:
                    return "orange"
                elif i in [2, 4, 6, 7, 8]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_ood":
                if i in [5]:
                    return "orange"
                elif i in [0, 2, 3, 4, 6, 7, 8]:
                    return "red"
                else:
                    return "green"
                
    elif fig_name == 'fig7a':
        def get_color(method, i):
            if method=="clip":
                if i in [2]:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="nd":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="milan_b":
                if i in [0, 2, 4, 7]:
                    return "orange"
                elif i in [1, 5, 6, 8, 9]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_ood":
                if i in [0, 6, 8]:
                    return "orange"
                elif i in [1, 2, 3, 4, 5, 7, 9]:
                    return "red"
                else:
                    return "green"
                
    elif fig_name == 'fig7b':
        def get_color(method, i):
            if method=="clip":
                if i in []:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="nd":
                if i in [2,6]:
                    return "orange"
                elif i in [3,4]:
                    return "red"
                else:
                    return "green"
            elif method=="milan_b":
                if i in [0, 2, 3, 4, 6, 8, 9]:
                    return "orange"
                elif i in []:
                    return "red"
                else:
                    return "green"
            elif method=="milan_ood":
                if i in [3, 6, 8]:
                    return "orange"
                elif i in [0, 2, 4, 7, 9]:
                    return "red"
                else:
                    return "green"
    
    elif fig_name=='fig14a':
        def get_color(method, i):
            if method=="cos":
                if i in []:
                    return "orange"
                elif i in [0,1,3]:
                    return "red"
                else:
                    return "green"
            elif method=="soft_wpmi":
                return "green"
            
    
    elif fig_name=="fig14b":
        def get_color(method, i):
            if method=="cos":
                return "red"
            elif method=="soft_wpmi":
                return "green"
    
    else:
         def get_color(method, i):
            return "black"
        
    return get_color