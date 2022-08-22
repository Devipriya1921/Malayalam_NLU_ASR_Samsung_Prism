# Malayalam_NLU_ASR_Samsung_Prism

# ChatBot_ML

Requirements: Rasa version=2.8
              Spacy

Steps <br />
1. Download pre-trained fastText vector. <br />
   https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ml.300.vec.gz <br />
   
2. Convert the vector to spaCy model. <br />
   `python -m spacy init vectors ml ./cc.ml.300.vec.gz ./tmp/spacy_ml`
   
3. Pack the converted model. <br />
    Next, we would pack the model with the package command. Note that, we need to make the output folder first, then type the command. <br />
   *python -m spacy package [input_dir] [output_dir]* <br />
   <br />
   `python -m spacy package ./tmp/spacy_ml ./tmp/packed` <br />
    
4. Build the package <br />
    Then, we go to the directory of the packed model and build it.<br /> 
    <br />
    `cd tmp/packed/ml_pipeline-0.0.0` <br />
    <br />
    `python setup.py sdist` <br />
 
 5. Install the package <br />
     When building finished, we can install the package by pip. <br />
     <br />
     `pip install dist/ml_pipeline-0.0.0.tar.gz`
    <br />
 6. To run the bot  <br />
     i)Open two terminals side by side in the same root directory of ChatBot_ML  <br />
     ii)1st terminal window : Run `rasa run actions` <br />
         2nd terminal window : Run `rasa shell`  <br /> 
