#!/usr/bin/env python3
"""
Unified Solar Time (UST) Clock - Windows Desktop Application
A metric-based time system using Sol as the base unit

Hours display as whole numbers (0-9), not decimals
Format: H.MMSS (Centisol.Millisol.Microsol)
"""

import tkinter as tk
from tkinter import ttk
import datetime
import math

class UnifiedSolarTimeClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Unified Solar Time (UST) Clock")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        
        self.root.configure(bg="#2c3e50")
        
        self.setup_styles()
        self.create_widgets()
        self.update_time()
    
    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("TFrame", background="#2c3e50")
        style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1")
        style.configure("Title.TLabel", background="#2c3e50", foreground="#3498db", 
                       font=("Helvetica", 24, "bold"))
        style.configure("Subtitle.TLabel", background="#2c3e50", foreground="#95a5a6",
                       font=("Helvetica", 12))
        style.configure("Time.TLabel", background="#34495e", foreground="#2ecc71",
                       font=("Courier New", 48, "bold"))
        style.configure("Label.TLabel", background="#2c3e50", foreground="#bdc3c7",
                       font=("Helvetica", 10))
        style.configure("Result.TLabel", background="#2c3e50", foreground="#3498db",
                       font=("Courier New", 24, "bold"))
    
    def create_widgets(self):
        """Create UI widgets"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="Unified Solar Time", style="Title.TLabel").pack()
        ttk.Label(header_frame, text="Metric Time System ⊙", style="Subtitle.TLabel").pack()
        
        # Clock Section
        clock_frame = ttk.LabelFrame(main_frame, text="Current Time", padding=20)
        clock_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Standard time
        ttk.Label(clock_frame, text="Standard Time (UTC)", style="Label.TLabel").pack()
        self.standard_time_label = ttk.Label(clock_frame, text="00:00:00", 
                                            style="Time.TLabel")
        self.standard_time_label.pack(pady=(0, 20))
        
        # UST time
        ttk.Label(clock_frame, text="Unified Solar Time", style="Label.TLabel").pack()
        self.ust_time_frame = ttk.Frame(clock_frame)
        self.ust_time_frame.pack(pady=(0, 10))
        
        self.ust_hours = ttk.Label(self.ust_time_frame, text="0", style="Time.TLabel")
        self.ust_hours.pack(side=tk.LEFT)
        
        ttk.Label(self.ust_time_frame, text=".", foreground="#2ecc71", 
                 background="#34495e", font=("Courier New", 48, "bold")).pack(side=tk.LEFT)
        
        self.ust_minutes = ttk.Label(self.ust_time_frame, text="00", style="Time.TLabel")
        self.ust_minutes.pack(side=tk.LEFT)
        
        ttk.Label(self.ust_time_frame, text=".", foreground="#2ecc71",
                 background="#34495e", font=("Courier New", 48, "bold")).pack(side=tk.LEFT)
        
        self.ust_seconds = ttk.Label(self.ust_time_frame, text="00", style="Time.TLabel")
        self.ust_seconds.pack(side=tk.LEFT)
        
        ttk.Label(self.ust_time_frame, text=" S", foreground="#2ecc71",
                 background="#34495e", font=("Courier New", 36, "bold")).pack(side=tk.LEFT, padx=(5, 0))
        
        self.ust_decimal = ttk.Label(clock_frame, text="0.0000 S", style="Label.TLabel")
        self.ust_decimal.pack()
        
        # Converter Section
        converter_frame = ttk.LabelFrame(main_frame, text="Convert Standard Time to UST", padding=20)
        converter_frame.pack(fill=tk.X)
        
        # Input frame
        input_frame = ttk.Frame(converter_frame)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(input_frame, text="Enter Time:", style="Label.TLabel").pack()
        
        time_input_frame = ttk.Frame(input_frame)
        time_input_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Label(time_input_frame, text="HH", style="Label.TLabel").pack(side=tk.LEFT, padx=(0, 5))
        self.input_hours = ttk.Entry(time_input_frame, width=3, font=("Courier New", 12))
        self.input_hours.pack(side=tk.LEFT, padx=(0, 10))
        self.input_hours.insert(0, "12")
        self.input_hours.bind("<KeyRelease>", lambda e: self.convert_time())
        
        ttk.Label(time_input_frame, text="MM", style="Label.TLabel").pack(side=tk.LEFT, padx=(0, 5))
        self.input_minutes = ttk.Entry(time_input_frame, width=3, font=("Courier New", 12))
        self.input_minutes.pack(side=tk.LEFT, padx=(0, 10))
        self.input_minutes.insert(0, "00")
        self.input_minutes.bind("<KeyRelease>", lambda e: self.convert_time())
        
        ttk.Label(time_input_frame, text="SS", style="Label.TLabel").pack(side=tk.LEFT, padx=(0, 5))
        self.input_seconds = ttk.Entry(time_input_frame, width=3, font=("Courier New", 12))
        self.input_seconds.pack(side=tk.LEFT)
        self.input_seconds.insert(0, "00")
        self.input_seconds.bind("<KeyRelease>", lambda e: self.convert_time())
        
        # Result
        ttk.Label(converter_frame, text="Result:", style="Label.TLabel").pack(anchor=tk.W, pady=(10, 5))
        self.result_label = ttk.Label(converter_frame, text="5.0000 S", style="Result.TLabel")
        self.result_label.pack(anchor=tk.W)
        
        # Info
        info_text = """• 1 Sol (S) = 1 full day (86,400 standard seconds)
• 1 Centisol = 4 standard hours  •  1 Millisol = 86.4 seconds  •  1 Microsol = 0.864 seconds"""
        ttk.Label(converter_frame, text=info_text, style="Label.TLabel", 
                 wraplength=600, justify=tk.LEFT).pack(anchor=tk.W, pady=(10, 0))
        
        self.convert_time()
    
    def standard_to_sol(self, hours, minutes, seconds):
        """Convert standard time to Sol time"""
        try:
            h = int(hours) if hours else 0
            m = int(minutes) if minutes else 0
            s = int(seconds) if seconds else 0
            
            if h > 23 or m > 59 or s > 59 or h < 0 or m < 0 or s < 0:
                return None
            
            # Total standard seconds
            total_std_seconds = h * 3600 + m * 60 + s
            
            # Convert to metric seconds (1 metric second = 0.864 standard seconds)
            total_metric_seconds = total_std_seconds / 0.864
            
            # Extract components
            centisols = int(total_metric_seconds / 10000)
            remainder = total_metric_seconds % 10000
            millisols = int(remainder / 100)
            microsols = int(remainder % 100)
            
            # Total decimal
            total_sols = total_metric_seconds / 100000
            
            return {
                'centisols': centisols,
                'millisols': millisols,
                'microsols': microsols,
                'total': total_sols
            }
        except (ValueError, TypeError):
            return None
    
    def convert_time(self):
        """Handle converter input"""
        result = self.standard_to_sol(
            self.input_hours.get(),
            self.input_minutes.get(),
            self.input_seconds.get()
        )
        
        if result:
            self.result_label.config(text=f"{result['total']:.4f} S")
        else:
            self.result_label.config(text="Invalid time")
    
    def update_time(self):
        """Update clock display"""
        now = datetime.datetime.utcnow()
        
        # Standard time
        std_time = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
        self.standard_time_label.config(text=std_time)
        
        # Convert to Sol
        result = self.standard_to_sol(now.hour, now.minute, now.second)
        
        if result:
            self.ust_hours.config(text=str(result['centisols']))
            self.ust_minutes.config(text=f"{result['millisols']:02d}")
            self.ust_seconds.config(text=f"{result['microsols']:02d}")
            self.ust_decimal.config(text=f"{result['total']:.4f} S")
        
        # Schedule next update
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = UnifiedSolarTimeClock(root)
    root.mainloop()
