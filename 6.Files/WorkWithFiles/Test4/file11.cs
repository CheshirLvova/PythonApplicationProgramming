using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            OpenPage(pages.HillCipher);
        }

        public enum pages
        {
            HillCipher,
            XORCipher
        }

        public void OpenPage(pages pages)
        {
            if (pages == pages.HillCipher)
            {
                frame.Navigate(new HillCipher(this));
            }
            else if (pages == pages.XORCipher)
            {
                frame.Navigate(new XORCipher(this));
            }
        }
    }
}
