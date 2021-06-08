using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Kovalchuk.HillAndHammaCiphers
{
    /// <summary>
    /// Interaction logic for HillCipher.xaml
    /// </summary>
    public partial class HillCipher : Page
    {
        public MainWindow mainWindow;
        private IDialogService dialogService;
        public EncryptMachine encryptMachine;
        public EncryptMachine decryptMachine;

        internal IDialogService DialogService { get => dialogService; set => dialogService = value; }

        public HillCipher(MainWindow _mainWindow)
        {
            InitializeComponent();
            DialogService = new DefaultDialogService();
            encryptMachine = new EncryptMachine();
            decryptMachine = new EncryptMachine();
            mainWindow = _mainWindow;
        }

        public void menuOpenFile_Click(object sender, RoutedEventArgs e)
        {
            if (DialogService.OpenFileDialog())
            {
                inputTextBox.Text = File.ReadAllLines(DialogService.FilePath).First();
                keyTextBox.Text = File.ReadAllLines(DialogService.FilePath).Skip(1).First();
            }
        }

        public void menuSaveFile_Click(object sender, RoutedEventArgs e)
        {
            if (!string.IsNullOrEmpty(DialogService.FilePath))
            {
                File.WriteAllText(DialogService.FilePath, outputTextBlock.Text + "\n" + keyTextBox.Text);
            }
            else
            {
                menuSaveFileAs_Click(sender, e);
            }
        }

        public void menuSaveFileAs_Click(object sender, RoutedEventArgs e)
        {
            if (DialogService.SaveFileDialog())
            {
                File.WriteAllText(DialogService.FilePath, outputTextBlock.Text + "\n" + keyTextBox.Text);
                //File.WriteAllText(dialogService.FilePath, inputTextBox.Text + "\n" + outputTextBlock.Text + "\n");
            }
        }

        public void HillCipher_Click(object sender, RoutedEventArgs e)
        {
            mainWindow.OpenPage(MainWindow.pages.HillCipher);
        }

        public void XORCipher_Click(object sender, RoutedEventArgs e)
        {
            mainWindow.OpenPage(MainWindow.pages.XORCipher);
        }

        public void Info_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("                                       Лабораторна робота 2\n" +
                "                                       Практична частина.\n" +
                "1. Створіть криптографічну систему, яка використовує шифр  Хілла, описаний у теоретичній частині.\n" +
                "2. Система шифрування повинна задовольняти наступним вимогам: 1) читати відкрите повідомлення з текстового файлу і перетворювати його у цифрове представлення; 2) запитувати ключове слово(9 і більше літер); 3) генерувати ключ-матрицю по ключовому слову; 4) шифрувати за допомогою алгоритму Хілла відкрите повідомлення і записувати його у файл.\n" +
                "3. Система розшифровування повинна задовольняти таким вимогам: 1) читати шифрограму з текстового файлу; 2) запитувати ключове слово; 3) генерувати ключ-матрицю; 4) розшифровувати шифрограму і виводити її у файл та на екран монітора.\n" +
               "HILL CIPHER (by Sofia Kovalchuk, PMI-44)");
        }

        public void inputTextBox_TextChanged(object sender, RoutedEventArgs e)
        {

        }

        public void menuNewFile_Click(object sender, RoutedEventArgs e)
        {
            inputTextBox.Text = "";
        }

        private void inputTextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void inputTextBox_SourceUpdated(object sender, DataTransferEventArgs e)
        {

        }

        private void inputTextBox_TargetUpdated(object sender, DataTransferEventArgs e)
        {

        }

        private void EncryptButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                
                if (keyTextBox.Text == "")
                {
                    outputTextBlock.Text = "";
                    for (int i = 0; i < 29; i++)
                    {
                        outputTextBlock.Text += encryptMachine.encryptText(inputTextBox.Text, i.ToString());
                        outputTextBlock.Text += "\n\n\n";
                    }
                }
                else
                {
                    outputTextBlock.Text = encryptMachine.encryptText(inputTextBox.Text, keyTextBox.Text);
                }
            }
            catch (Exception ex)
            {
                DialogService.ShowMessage(ex.Message);
            }
        }

        private void DecryptButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                if (keyTextBox.Text == "")
                {
                    outputTextBlock.Text = "";
                    for (int i = 0; i < 29; i++)
                    {
                        outputTextBlock.Text += decryptMachine.encryptText(inputTextBox.Text, i.ToString());
                        outputTextBlock.Text += "\n\n\n";
                    }
                }
                else
                {
                    outputTextBlock.Text = decryptMachine.decryptText(inputTextBox.Text, keyTextBox.Text);
                }
            }
            catch (Exception ex)
            {
                DialogService.ShowMessage(ex.Message);
            }
        }

        private void ComboBoxEncryptionType_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }
    }
}
