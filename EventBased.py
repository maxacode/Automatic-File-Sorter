
try:

    import os, time, sys
    # sys.path.append(os.getcwd()+"\\" + 'venv'+'\\'+'Lib'+'\\'+'site-packages')

    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer


    class MyHandler(FileSystemEventHandler):
        print("Class stared")
        i = 1
        def on_modified(self, event):
            print("Function started")
            for filename in os.listdir(folder_to_track):
                new_name = filename
                print("Iterating for ech file")
                if filename != "EventBased.py" and filename != 'transfered':
                    file_exists = os.path.isfile(folder_to_transfer + "\\" + new_name)
                    while file_exists:
                        print("White loop to ")
                        self.i += 1
                        new_name = "New_File_" + str(self.i)+".txt"
                        print(new_name)
                        file_exists = os.path.isfile(folder_to_transfer + "\\"+new_name)
                        print(file_exists)
                    print("Startig transfer")
                    src = folder_to_track + "\\" + filename
                    new_dest = folder_to_transfer + "\\" + new_name
                    time.sleep(2)
                    try:
                        os.rename(src, new_dest)

                    except Exception as error:
                        print('Error on transfering file: {}'.format(error))
                        continue
                    print("Transfer done: {}".format(filename))

    folder_to_track = r"C:\Users\14175\Downloads\test"
    folder_to_transfer = r"C:\Users\14175\Downloads\test\transfered"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

except Exception as error:
    print(error)
    input(" ")
