# DS-Checker (DocSim)
  
#### Project Goal: ####  
  
The goal of the document similarity checker project is to develop a tool that can determine the similarity between two text documents. The project aims to compare the content of the documents and provide a similarity score, helping users to identify duplicate or similar documents.

#### Technical Details: ####  
  
  * Programming language used: Python, PHP  
  * Required libraries and packages: math,re,sys,collections.Counter  
  * Algorithm used: Cosine Similarity  
  * Input format: text files  
  
#### Instructions: ####  

1. Clone the repository or download the source code.
2. Install the required libraries and packages specified in the "Technical Details" section
3. Copy all contents in WAMP's www folder/XAMPP's htdocs folder and create a virtual host in corresponding web server package.
4. Access the virtual host created in previous step. It would look like this:
![index](https://user-images.githubusercontent.com/91898207/141613472-8307a3f6-81b2-464a-a812-4dc068a47c00.jpg)
The text documents can be uploaded from this webpage
5. Choose two text files and click on "Upload".
6. The output will be displayed in same browser window displaying a cosine distance.  
Cosine Similarity = 1 - Cosine Distance  
Similarity Percentage = Cosine Similarity * 100

![upres](https://user-images.githubusercontent.com/91898207/141613496-19e1f8c8-2aaf-4d11-8d84-3db63369c03a.jpg)
The files would be uploaded and send to python as arguments 

Elevator pitch can be found here
https://github.com/sud0x00/DS-Checker/blob/0860d0f29435b0b8ee95b0384e325c1ff8918e8a/src/Elevator%20Pitch.pdf
(src/Elevator Pitch.pdf)


