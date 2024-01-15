import cv2,time

names = ['Yassir','Abra','Haji','Ali','Yasir','Aba','Hai','li']

for index, name in enumerate(names):
    cerificate = cv2.imread('egazCertificate.jpg')
    start_time = time.time()
    cv2.putText(cerificate, name, (1953, 1451), cv2.FONT_HERSHEY_SIMPLEX , 8, (0, 0, 255),4, cv2.LINE_AA)

    # bracket za mwanzo ni sehem ya kutia text yangu,
    # mbele yake kuna font,
    # halaf color
    # halaf thickness 

    # pa kuweka certifucates
    cv2.imwrite(f'D:\project\certificateAutomation\Generated Certificates\{name}.jpg', cerificate)

    print('Processing Certificate {}/{}'.format(index+1, len(names)))
end_time = time.time()
taken_time = end_time - start_time

print(f'Process completed \n{len(names)} certificates generated within {taken_time:.3f} seconds') 