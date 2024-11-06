import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import numpy as np

class VideoToAscii:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertisseur Vidéo en ASCII")
        self.ASCII_CHARS = "@%#*+=-:. "
        self.video_path = None
        self.cap = None
        self.is_playing = False
        self.aspect_ratio = "16:9"
        self.width = 100
        self.create_widgets()
        
    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both', padx=10, pady=5)
        
        self.top_controls = ttk.Frame(self.main_frame)
        self.top_controls.pack(fill='x', pady=5)
        
        self.select_btn = ttk.Button(
            self.top_controls, 
            text="Choisir une vidéo", 
            command=self.select_video
        )
        self.select_btn.pack(side=tk.LEFT, padx=5)
        
        self.format_frame = ttk.LabelFrame(self.top_controls, text="Format")
        self.format_frame.pack(side=tk.LEFT, padx=20)
        
        self.aspect_var = tk.StringVar(value="auto")
        ttk.Radiobutton(self.format_frame, text="Auto", variable=self.aspect_var, 
                       value="auto", command=self.update_display).pack(side=tk.LEFT)
        ttk.Radiobutton(self.format_frame, text="16:9", variable=self.aspect_var, 
                       value="16:9", command=self.update_display).pack(side=tk.LEFT)
        ttk.Radiobutton(self.format_frame, text="4:3", variable=self.aspect_var, 
                       value="4:3", command=self.update_display).pack(side=tk.LEFT)
        
        self.width_frame = ttk.LabelFrame(self.top_controls, text="Largeur ASCII")
        self.width_frame.pack(side=tk.LEFT, padx=20)
        
        self.width_var = tk.IntVar(value=100)
        self.width_scale = ttk.Scale(
            self.width_frame,
            from_=50,
            to=200,
            orient=tk.HORIZONTAL,
            variable=self.width_var,
            command=lambda _: self.update_display()
        )
        self.width_scale.pack(side=tk.LEFT, padx=5)
        
        self.text_display = tk.Text(
            self.main_frame,
            font=('Courier', 8),
            wrap=tk.NONE
        )
        self.text_display.pack(expand=True, fill='both')
        
        self.x_scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.HORIZONTAL, 
                                       command=self.text_display.xview)
        self.x_scrollbar.pack(fill=tk.X)
        self.y_scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                       command=self.text_display.yview)
        self.y_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.text_display.configure(
            xscrollcommand=self.x_scrollbar.set,
            yscrollcommand=self.y_scrollbar.set
        )
        
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(fill='x', pady=5)
        
        self.play_btn = ttk.Button(
            self.controls_frame,
            text="Lecture",
            command=self.toggle_play
        )
        self.play_btn.pack(side=tk.LEFT, padx=5)
        
        self.progress = ttk.Scale(
            self.controls_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.seek_video
        )
        self.progress.pack(side=tk.LEFT, padx=5, expand=True, fill='x')
        
        self.status_var = tk.StringVar(value="Prêt")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var)
        self.status_label.pack(pady=5)
    
    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Fichiers vidéo", "*.mp4 *.avi *.mkv *.mp3  ")]
        )
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.progress['to'] = self.total_frames
            self.update_status()
            self.update_display()
    
    def calculate_dimensions(self, frame):
        base_width = self.width_var.get()
        if self.aspect_var.get() == "auto":
            ratio = frame.shape[1] / frame.shape[0]
        elif self.aspect_var.get() == "16:9":
            ratio = 16/9
        else:
            ratio = 4/3
        height = int((base_width / ratio) * 0.55)
        return base_width, height
    
    def image_to_ascii(self, image):
        width, height = self.calculate_dimensions(image)
        resized = cv2.resize(image, (width, height))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        ascii_str = ''
        for row in gray:
            for pixel_value in row:
                ascii_str += self.ASCII_CHARS[pixel_value * len(self.ASCII_CHARS) // 256]
            ascii_str += '\n'
        return ascii_str
    
    def update_display(self):
        if self.cap is None:
            return
        current_pos = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        ret, frame = self.cap.read()
        if ret:
            ascii_frame = self.image_to_ascii(frame)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(1.0, ascii_frame)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_pos)
    
    def seek_video(self, value):
        if self.cap:
            frame_no = int(float(value))
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            self.update_display()
    
    def toggle_play(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.play_btn.configure(text="Pause")
            self.play_video()
        else:
            self.play_btn.configure(text="Lecture")
    
    def play_video(self):
        if not self.is_playing or self.cap is None:
            return
        ret, frame = self.cap.read()
        if ret:
            ascii_frame = self.image_to_ascii(frame)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(1.0, ascii_frame)
            current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.progress.set(current_frame)
            self.update_status()
            self.root.after(40, self.play_video)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.is_playing = False
            self.play_btn.configure(text="Lecture")
    
    def update_status(self):
        if self.cap:
            current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            current_time = current_frame / fps
            total_time = self.total_frames / fps
            self.status_var.set(f"Frame: {current_frame}/{self.total_frames} - "
                              f"Temps: {current_time:.1f}s/{total_time:.1f}s")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToAscii(root)
    root.mainloop()