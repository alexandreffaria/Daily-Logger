import time
import datetime
import win32gui

w = win32gui
janelaInicial = w.GetWindowText(w.GetForegroundWindow())
startClock = datetime.datetime.now()
endClock = datetime.datetime.now()

def confereJanelaAtiva():
    return w.GetWindowText(w.GetForegroundWindow())

while True:
    janelaAtiva = confereJanelaAtiva()
    
    if janelaInicial != janelaAtiva:
        startClock = datetime.datetime.now()
        janelaInicial = janelaAtiva
    
    else:
        endClock = datetime.datetime.now()

    duracao = endClock - startClock
    evento = { 
        "janela" : janelaAtiva,
        "duracao" : duracao
    }
    
    print(evento)

    time.sleep(1)


# while True:
#     janelaAtiva = w.GetWindowText(w.GetForegroundWindow())
#     horaAtual = datetime.datetime.now()
#     print(horaAtual)
#     print(janelaAtiva)
#     time.sleep(1)




# current_window = w.GetWindowText(w.GetForegroundWindow())
# start_time = None

# def foreground_window_changed(prev_foreground_window, new_foreground_window):
#     global current_window, start_time

#     if prev_foreground_window != new_foreground_window:
#         if current_window:
#             print(f"Duration spent on {current_window}: {time.time() - start_time} seconds")

#         current_window = win32gui.GetWindowModuleFileName(new_foreground_window)
#         start_time = time.time()

# while True:
#     print(current_window)
#     print(start_time)
#     foreground_window_handle = w.GetWindowText(w.GetForegroundWindow())
#     foreground_window_changed(foreground_window_handle, w.GetWindowText(w.GetForegroundWindow()))
#     time.sleep(0.5)



