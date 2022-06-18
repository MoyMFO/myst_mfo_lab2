## Description
*This project has been created to show the operation of two price explanatory models in the microstructure. On the one hand, the APT model that analyzes prices as a martingale stochastic process. On the other hand, the Roll model that aims to calculate the theoretical spread from transaction price data. Through considering the order book as an object that contains the data on which the model is based, the pertinent classes were made to calculate and plot the models.*

## Install dependencies

Install all the dependencies stated in the requirements.txt file, just run the following command in terminal:

        pip install -r requirements.txt
        
Or you can manually install one by one using the name and version in the file.

## Funcionalities

This project is about the testing and showcase of two pricing models for microstructure.
There is a class for pricing models available which contains methods for the APT and ROLL models calculations.

### Data to be used: 

A JSON files with orderbooks with timestamp, bid, and ask.

### Instances: Data preparation
data = DataPreparation()
order_books_data = data.order_books_json_transformation('orderbooks_05jul21.json')
### Instances: Models
model = PricingModelsOB(order_books_data)
### Call models
model.apt_model('mid_price', by='1T')
model.apt_model('weighted_midprice', by='1T')
model.roll_model()


### IMPORTANT:
main.py only shows the calling of models as a testing/proof of working.
Find detials and plots in Jupyter notebook.

## Author
Moises Flores Ortiz. Student of financial engineering about to graduate.

## License
**GNU General Public License v3.0** 

*Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license notices 
must be preserved. Contributors provide an express grant of patent rights.*

## Contact
*For more information in reggards of this repo, please contact if722183@iteso.mx*
