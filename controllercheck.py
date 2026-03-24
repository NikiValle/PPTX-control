import keyboard
print("Controller check")
print("Premi i tasti sul telecomando USB per vedere il segnale.")
print("Premi ESC per uscire.\n")
def report_event(event):
    if event.event_type == 'down':
        print(f"ID Segnale: {event.scan_code} | Tasto: '{event.name}'")
keyboard.hook(report_event)
keyboard.wait('esc')