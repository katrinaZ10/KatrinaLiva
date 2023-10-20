#ar skolotāju izskaidrots
nenodots = input("Vai jums ir kāds nenodots izdevums? (ja/ne)")
if nenodots == "ja":
    print("Jūs nedrīktat neko izņemt.")
elif nenodots == "ne":
    pieprasits = input("Vai šī publikācija ir pieprasīta? (ja/ne)")
    if pieprasits == "ja":
        print("Izsniedz uz 2 dienām.")
    elif pieprasits == "ne":
        zurnals = input("Vai publikācija ir žurnāls? (ja/ne)")
        if zurnals == "ja":
            print("Izsniegt uz 7 dienām.")
        elif zurnals == "ne":
            students = input("Vai jūs esat students? (ja/ne)")
            if students == "ja":
                print("Izsniedz uz 14 dienām.")
                if students == "ne":
                    print("Izsniedz uz 28 dienām.")

