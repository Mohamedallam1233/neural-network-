from numpy import*
import numpy as np
from  tkinter import*
from tkinter import ttk
from tkinter import messagebox
form = Tk()
form.title("neural network")
form.config(background="light blue")
Label(form, text="choice neural network",font=(12), fg="dark blue", bg="light blue").grid(row=0, column=0, padx=20, pady=20)
long = ttk.Combobox(form,values=("hetero_associative_memory","auto_associative","iterative_auto_associative","BAM"),font=(12))
long.grid(row=0, column=1)
def generate():
    x = long.get()
    if x == "hetero_associative_memory":
        Label(form, text="(p,sc,sr,tc,tr)", font=(12), fg="dark blue", bg="light blue").grid(row=2, column=0,padx=20, pady=20)
        frame=Frame(form)
        frame.config(background="light blue")
        pp = Entry(frame, font=(10), bd=5, bg="light blue",width=5)
        pp.grid(row=0, column=0)
        scc = Entry(frame, font=(10), bd=5, bg="light blue",width=5)
        scc.grid(row=0, column=1)
        srr = Entry(frame, font=(10), bd=5, bg="light blue",width=5)
        srr.grid(row=0, column=2)
        tcc = Entry(frame, font=(10), bd=5, bg="light blue",width=5)
        tcc.grid(row=0, column=3)
        trr = Entry(frame, font=(10), bd=5, bg="light blue",width=5)
        trr.grid(row=0, column=4)
        frame.grid(row=2, column=1)
        def getattribute():
            c = list()
            cc = list()
            collect_matrix = list()
            p = int(pp.get())
            sc = int(scc.get())
            sr = int(srr.get())
            tc = int(tcc.get())
            tr = int(trr.get())
            c = list()
            cc = list()
            collect_matrix = list()
            frame1 = Frame(form)
            frame1.config(background="light blue")
            frame2 = Frame(form)
            frame2.config(background="light blue")
            def fill_empty(a):
                empty = Entry(frame1,font=(10), bd=5, bg="light blue",width=10)
                empty.grid(row=0, column=a)
                return empty
            listOfEntries = [fill_empty(idx) for idx in range(int(p))]
            def fill_empty_store(a):
                empty = Entry(frame1,font=(10), bd=5, bg="light blue",width=10)
                empty.grid(row=1, column=a)
                return empty
            listOfEntries_store = [fill_empty_store(idx) for idx in range(int(p))]
            frame1.grid(row=4, column=1)
            frame2.grid(row=5, column=1)
            frame3 = Frame(form)
            frame3.config(background="light blue")
            Label(frame3, text="s ---->", font=(12), fg="dark blue", bg="light blue").grid(row=0, column=0)
            Label(frame3, text="t ---->", font=(12), fg="dark blue", bg="light blue").grid(row=1, column=0)
            frame3.grid(row=4, column=0, padx=10, pady=10)
            def fun_store():
                for i in range(p):
                    entries = [int(a) for a in listOfEntries[i].get().split()]
                    arr1 = np.array(entries).reshape(sr, sc)
                    c.append(arr1)
                    entries_t = [int(a) for a in listOfEntries_store[i].get().split()]
                    arr2 = np.array(entries_t).reshape(tr, tc)
                    cc.append(arr2)
                for i in range(0, p):
                    collect_matrix.append(np.dot(c[i].transpose(), cc[i]))
                shape = np.shape(np.dot(c[0].transpose(), cc[0]))
                w = np.full(shape, 0)
                for i in collect_matrix:
                    w += i
                frame4 = Frame(form)
                Label(frame4, text="weight matrix = ", font=(12), fg="dark blue").grid(row=0, column=0 , padx=5)
                Label(frame4, text=w, font=(12), fg="dark blue").grid(row=0, column=1)
                frame4.grid(row=7, column=0, columnspan=2)
                frame5 = Frame(form)
                frame5.config(background="light blue")
                Label(frame5, text="enter test pattern", font=(12), fg="dark blue", bg="light blue").grid(row=0, column=0, padx=5)
                test = Entry(frame5, font=(10), bd=5, bg="light blue", width=5)
                test.grid(row=0, column=1)
                def res():
                    tt=test.get()
                    x = [int(a) for a in tt.split()]
                    result = np.dot(x, w)
                    final_result = list()
                    for i in result:
                        if i > 0:
                            final_result.append(1)
                        else:
                            final_result.append(0)
                    frame6 = Frame(form)
                    Label(frame6, text="test result = ", font=(12), fg="dark blue").grid(row=0, column=0, padx=5)
                    Label(frame6, text=final_result, font=(12), fg="dark blue").grid(row=0, column=1)
                    frame6.grid(row=10, column=0, columnspan=2)
                Button(frame5, text="result", bd=6, bg="dark blue", fg="white", activebackground='Gray',activeforeground='light blue', command=res).grid(row=9, column=0, columnspan=2, padx=10,pady=10)

                frame5.grid(row=8, column=0, columnspan=2 , padx=10 , pady=10)
            Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray', activeforeground='light blue', command=fun_store).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray',
               activeforeground='light blue', command=getattribute).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    if x == "auto_associative":
        Label(form, text="(pattern,yc,yr)", font=(12), fg="dark blue", bg="light blue").grid(row=2, column=0, padx=20,
                                                                                             pady=20)
        frame = Frame(form)
        frame.config(background="light blue")
        pp = Entry(frame, font=(10), bd=5, bg="light blue", width=10)
        pp.grid(row=0, column=0)
        scc = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        scc.grid(row=0, column=1)
        srr = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        srr.grid(row=0, column=2)
        frame.grid(row=2, column=1)
        def gerattribute():
            R=int(srr.get())
            C=int(scc.get())
            p=pp.get()
            entries = [int(a) for a in p.split()]
            arr1 = np.array(entries).reshape(R, C)
            arr1_transpose = arr1.transpose()
            w = np.dot(arr1_transpose, arr1)
            frame = Frame(form)
            Label(frame, text="weight matrix = ", font=(12), fg="dark blue").grid(row=0, column=0, padx=5)
            Label(frame, text=w, font=(12), fg="dark blue").grid(row=0, column=1)
            frame.grid(row=4, column=0, columnspan=2)
            frame1 = Frame(form)
            frame1.config(background="light blue")
            Label(frame1, text="enter test pattern", font=(12), fg="dark blue", bg="light blue").grid(row=0, column=0,padx=5)
            test = Entry(frame1, font=(10), bd=5, bg="light blue", width=10)
            test.grid(row=0, column=1)
            frame1.grid(row=5, column=0, columnspan=2)
            def res():
                tt = test.get()
                x = [int(a) for a in tt.split()]
                result = np.dot(x, w)
                final = list()
                for i in result:
                    if i > 0:
                        final.append(1)
                    elif i < 0:
                        final.append(-1)
                    else:
                        final.append(0)
                frame2 = Frame(form)
                Label(frame2, text="test result = ", font=(12), fg="dark blue").grid(row=0, column=0, padx=5)
                Label(frame2, text=final, font=(12), fg="dark blue").grid(row=0, column=1)
                frame2.grid(row=7, column=0, columnspan=2)
            Button(form, text="result", bd=6, bg="dark blue", fg="white", activebackground='Gray',activeforeground='light blue', command=res).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray',activeforeground='light blue', command=gerattribute).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    if x == "iterative_auto_associative":
        Label(form, text="(pattern,yc,yr,p)", font=(12), fg="dark blue", bg="light blue").grid(row=2, column=0, padx=20,pady=20)
        frame = Frame(form)
        frame.config(background="light blue")
        pp = Entry(frame, font=(10), bd=5, bg="light blue", width=10)
        pp.grid(row=0, column=0)
        scc = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        scc.grid(row=0, column=1)
        srr = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        srr.grid(row=0, column=2)
        nn = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        nn.grid(row=0, column=3)
        frame.grid(row=2, column=1)
        def gerattribute():
            R = int(srr.get())
            C = int(scc.get())
            p = pp.get()
            n=int(nn.get())
            entries = [int(a) for a in p.split()]
            arr1 = np.array(entries).reshape(R, C)
            arr1_transpose = arr1.transpose()
            w = np.dot(arr1_transpose, arr1) - np.eye(C)*n
            frame = Frame(form)
            Label(frame, text="weight matrix = ", font=(12), fg="dark blue").grid(row=0, column=0, padx=5)
            Label(frame, text=w, font=(12), fg="dark blue").grid(row=0, column=1)
            frame.grid(row=4, column=0, columnspan=2)
            frame1 = Frame(form)
            frame1.config(background="light blue")
            Label(frame1, text="enter test pattern", font=(12), fg="dark blue", bg="light blue").grid(row=0, column=0,
                                                                                                      padx=5)
            test = Entry(frame1, font=(10), bd=5, bg="light blue", width=10)
            test.grid(row=0, column=1)
            frame1.grid(row=5, column=0, columnspan=2)

            def res():
                tt = test.get()
                x = [int(a) for a in tt.split()]
                result = np.dot(x, w)
                final = list()
                for i in result:
                    if i > 0:
                        final.append(1)
                    elif i < 0:
                        final.append(-1)
                    else:
                        final.append(0)
                frame2 = Frame(form)
                if array(final).all() != arr1.all() : final = np.dot(final,w)
                Label(frame2, text="test result = ", font=(12), fg="dark blue").grid(row=0, column=0, padx=5)
                Label(frame2, text=final, font=(12), fg="dark blue").grid(row=0, column=1)
                frame2.grid(row=7, column=0, columnspan=2)

            Button(form, text="result", bd=6, bg="dark blue", fg="white", activebackground='Gray', activeforeground='light blue', command=res).grid(row=6, column=0, columnspan=2, padx=10,pady=10)

        Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray',activeforeground='light blue', command=gerattribute).grid(row=3, column=0, columnspan=2, padx=10,pady=10)
    if x == "BAM":
        Label(form, text="(p,fc,fr,sc,sr)", font=(12), fg="dark blue", bg="light blue").grid(row=2, column=0, padx=20, pady=20)
        frame = Frame(form)
        frame.config(background="light blue")
        pp = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        pp.grid(row=0, column=0)
        scc = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        scc.grid(row=0, column=1)
        srr = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        srr.grid(row=0, column=2)
        tcc = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        tcc.grid(row=0, column=3)
        trr = Entry(frame, font=(10), bd=5, bg="light blue", width=5)
        trr.grid(row=0, column=4)
        frame.grid(row=2, column=1)
        def getfun():
            numper_of_pair = int(pp.get())
            f_pair_c = int(scc.get())
            f_pair_r = int(srr.get())
            s_pair_c = int(tcc.get())
            s_pair_r = int(trr.get())
            c = list()
            cc = list()
            collect_matrix = list()
            frame1 = Frame(form)
            frame1.config(background="light blue")
            frame2 = Frame(form)
            frame2.config(background="light blue")

            def fill_empty(a):
                empty = Entry(frame1, font=(10), bd=5, bg="light blue", width=10)
                empty.grid(row=0, column=a)
                return empty

            listOfEntries = [fill_empty(idx) for idx in range(int(numper_of_pair))]

            def fill_empty_store(a):
                empty = Entry(frame1, font=(10), bd=5, bg="light blue", width=10)
                empty.grid(row=1, column=a)
                return empty

            listOfEntries_store = [fill_empty_store(idx) for idx in range(int(numper_of_pair))]
            frame1.grid(row=4, column=1)
            frame2.grid(row=5, column=1)
            frame3 = Frame(form)
            frame3.config(background="light blue")
            Label(frame3, text="s ---->", font=(12), fg="dark blue", bg="light blue").grid(row=0, column=0)
            Label(frame3, text="t ---->", font=(12), fg="dark blue", bg="light blue").grid(row=1, column=0)
            frame3.grid(row=4, column=0, padx=10, pady=10)
            def fun_store():
                for i in range(numper_of_pair):
                    entries = [int(a) for a in listOfEntries[i].get().split()]
                    arr1 = np.array(entries).reshape(f_pair_r, f_pair_c)
                    c.append(arr1)
                    entries_t = [int(a) for a in listOfEntries_store[i].get().split()]
                    arr2 = np.array(entries_t).reshape(s_pair_r, s_pair_c)
                    cc.append(arr2)
                for i in range(numper_of_pair):
                    collect_matrix.append(np.dot(c[i], cc[i].transpose()))
                shape = np.shape(np.dot(c[0], cc[i].transpose()))
                w = np.full(shape, 0)
                for i in collect_matrix:
                    w += i
                frame4 = Frame(form)
                Label(frame4, text="weight matrix = ", font=(12), fg="dark blue").grid(row=0, column=0 , padx=5)
                Label(frame4, text=w, font=(12), fg="dark blue").grid(row=0, column=1)
                frame4.grid(row=7, column=0, columnspan=2)
                for i in range(0, numper_of_pair):
                    y = array(sign(dot(w.transpose(), c[i])))
                    if (y != cc[i]).all():
                        c[i] = dot(w, cc[i])
                    x = array(sign(dot(w, cc[i])))
                    if (x != c[i]).all():
                        cc[i] = dot(w.transpose(), c[i])
            Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray', activeforeground='light blue', command=fun_store).grid(row=6, column=0, columnspan=2, padx=10,pady=10)
        Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray',activeforeground='light blue', command=getfun).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    if x=="":messagebox.showerror("error","choice any answer")
Button(form, text="ok", bd=6, bg="dark blue", fg="white", activebackground='Gray',activeforeground='light blue',command=generate).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
form.mainloop()