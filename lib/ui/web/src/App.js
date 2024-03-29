import { Router, Nav } from './components'
function App() {
  const path = window.location.pathname;
  return (
    <section className='h-screen w-screen bg-slate-700 flex flex-col overflow-hidden'>
      <Nav />
      <Router path={path} />
    </section>

  )
}

export default App;