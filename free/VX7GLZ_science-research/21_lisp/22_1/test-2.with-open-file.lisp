(setq fname "data-2.dat")

(with-open-file (stream fname :direction :output)
		(format stream "Usual tasks involving computer engineers include writing software and firmware for embedded microcontrollers, designing VLSI chips, designing analog sensors, designing mixed signal circuit boards, and designing operating systems. ")
		(terpri stream)
		(format stream "Computer engineers are also suited for robotics research, which relies heavily on using digital systems to control and monitor electrical systems like motors, communications, and sensors.")
		(terpri stream))
