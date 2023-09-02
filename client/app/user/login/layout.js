import '../../globals.css'
import { Roboto } from 'next/font/google';

const inter = Roboto({ weight:'400', subsets:['greek'] })

export const metadata = {
  title: 'Procord | Login',
  description: 'Dive into a new world of messaging',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <main className= "app bg-stone-900 w-screen h-screen flex justify-center align-middle items-center">
          {children}
        </main>
      </body>
    </html>
  )
}
