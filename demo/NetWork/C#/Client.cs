using System;
using System.IO;
using System.Net;
using System.Net.Sockets;

namespace Queen {
	class NetWork {
		public static void Main() {
			try {
				TcpClient tcpClient = new TcpClient();
				Console.WriteLine("Connecting....");
				
				tcpClient.Connect("104.236.139.161",  21576);
				
				Console.WriteLine("Connected");
				NetworkStream stream = tcpClient.GetStream();
					
				while (true)
				{
					Console.Write("Enter the string to be transmitted : ");
					
					string str = Console.ReadLine();
					
					Byte[] data = System.Text.Encoding.ASCII.GetBytes(str);
					
					//Send the message to the connected TcpServer.
					stream.Write(data, 0, data.Length);
					
					Console.WriteLine("Sent: {0}", str);
					
					data = new Byte[10];
					
					string responeData = String.Empty;
					Int32 bytes = stream.Read(data, 0, data.Length);

					responeData = System.Text.Encoding.ASCII.GetString(data, 0, bytes);
					Console.WriteLine("Received: {0}", responeData);
				}
				stream.Close();
				tcpClient.Close();
			}
			catch (ArgumentNullException e)
			{
				Console.WriteLine("SocketException: {0}", e);
			}
			catch (SocketException e)
			{
				Console.WriteLine("SocketException: {0}", e);
			}
		}
	}
}
