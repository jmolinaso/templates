;;;; commandline.lisp
;To have into considerationg about getopt
; define if the parameter is unique
; define if the parameter has one value
; define if the paramater has some values
(load "~/.clisprc.lisp")

(defun findoption (command args)
	"Check whether the command is in the arguments"
	(cond 
		((null args) nil)
		((equal command (car args)) t)
		((consp (car args)) (or (findoption command (car args))
								(findoption command (cdr args))))
		(t (findoption command (cdr args)))))

(format t  "~S~%" (findoption "b" *args*))


;;; here comes commandline.
