import time 
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"تم تعيين المنبه على {alarm_time}")
    
    sound_file = "mysound.mp3"  # تأكد من وجود ملف الصوت في نفس المجلد أو تحديد المسار الصحيح
    is_running = True


    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"الوقت الحالي: {current_time}")

        if current_time == alarm_time:
            print("المنبه! الوقت الآن")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
    
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("أدخل وقت المنبه (HH:MM): ")
    set_alarm(alarm_time)
