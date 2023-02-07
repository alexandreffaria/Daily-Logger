import time
import datetime
import win32gui
import json
import win32api

w = win32gui
janelaInicial = w.GetWindowText(w.GetForegroundWindow())
startClock = datetime.datetime.now()
endClock = datetime.datetime.now()
last_mouse_movement = win32api.GetTickCount()


def confereJanelaAtiva():
    return w.GetWindowText(w.GetForegroundWindow())


def mouse_idle_time():
    return (win32api.GetTickCount() - last_mouse_movement) / 1000.0


while True:
    janelaAtiva = confereJanelaAtiva()

    if janelaInicial != janelaAtiva:
        endClock = datetime.datetime.now()
        duracao = (endClock - startClock).total_seconds()
        evento = {
            "janela": janelaInicial,
            "start": str(startClock),
            "end": str(endClock),
            "duracao": duracao
        }
        if evento["duracao"] >= 10:
            if mouse_idle_time() < 600:
                with open('events.json', 'a') as f:
                    json.dump(evento, f)
                    f.write('\n')
            else:
                print("Evento removido por inatividade")
        startClock = datetime.datetime.now()
        janelaInicial = janelaAtiva
        last_mouse_movement = win32api.GetTickCount()

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
