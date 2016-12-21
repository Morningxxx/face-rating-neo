def getData(f):
    res = f['landmark']

    ssss = ''

    for s in res.keys():
        x = str(res[s]['x'])
        y = str(res[s]['y'])
        ssss = ssss + x + ", "
        ssss = ssss + y + ", "

    attr = f['attributes']
    for a in attr.keys():
        if a == 'gender':
            if attr[a]['value'] == 'Female':
                ssss = ssss + "0" + ", "
            else:
                ssss = ssss + "1" + ", "
        if a == 'age':
            s1 = str(attr[a]['value'])
            ssss = ssss + s1 + ", "
        if a == 'glass':
            if attr[a]['value'] == 'None':
                ssss = ssss + "0" + ", "
            else:
                ssss = ssss + "1" + ", "
        if a == 'headpose':
            s1 = str(attr[a]['yaw_angle'])
            s2 = str(attr[a]['pitch_angle'])
            s3 = str(attr[a]['roll_angle'])
            ssss = ssss + s1 + ", "
            ssss = ssss + s2 + ", "
            ssss = ssss + s3 + ", "
        if a == 'blur':
            gb = attr[a]['gaussianblur']
            s1 = str(gb['threshold'])
            s2 = str(gb['value'])
            ssss = ssss + s1 + ", "
            ssss = ssss + s2 + ", "

            mb = attr[a]['motionblur']
            s1 = str(mb['threshold'])
            s2 = str(mb['value'])
            ssss = ssss + s1 + ", "
            ssss = ssss + s2 + ", "

        if a == 'smile':
            smile = attr[a]
            s1 = str(smile['threshold'])
            s2 = str(smile['value'])
            ssss = ssss + s1 + ", "
            ssss = ssss + s2 + ", "

        if a == 'facequality':
            fq = attr[a]
            s1 = str(fq['threshold'])
            s2 = str(fq['value'])
            ssss = ssss + s1 + ", "
            ssss = ssss + s2 + ", "

    face_rec = f['face_rectangle']
    s1 = str(face_rec['width'])
    s2 = str(face_rec['top'])
    s3 = str(face_rec['height'])
    s4 = str(face_rec['left'])
    ssss = ssss + s1 + ", "
    ssss = ssss + s2 + ", "
    ssss = ssss + s3 + ", "
    ssss = ssss + s4 + ", " + "\n"

    return ssss

