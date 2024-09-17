import React from 'react'

const Login = () => {
  return (
    <div className="flex items-center justify-center h-screen bg-blue-500">
      {/* Left Section */}
      <div className="relative flex w-full h-full">
        <div className="absolute top-1/4 left-10 text-white">
          <h1 className="text-4xl font-bold">AIDD</h1>
          <h2 className="text-2xl font-semibold">SynCoOp</h2>
        </div>
      </div>

      {/* Right Section */}
      <div className="flex items-center justify-center">
        <div className="bg-white rounded-md shadow-lg p-8 w-96">
          <h2 className="text-xl font-bold text-center mb-6">Welcome!</h2>
          <form>
            <div className="mb-4">
              <label
                htmlFor="email"
                className="block text-gray-700 text-sm font-bold mb-2"
              >
                Email Address
              </label>
              <input
                type="email"
                id="email"
                placeholder="Enter your email"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              />
            </div>

            <div className="mb-6">
              <label
                htmlFor="password"
                className="block text-gray-700 text-sm font-bold mb-2"
              >
                Password
              </label>
              <input
                type="password"
                id="password"
                placeholder="Enter your password"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              />
            </div>

            <div className="flex items-center justify-between mb-6">
              <a
                href="#"
                className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
              >
                Forgot password?
              </a>
            </div>

            <div className="flex items-center justify-center">
              <button
                type="submit"
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              >
                Log In
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Login
